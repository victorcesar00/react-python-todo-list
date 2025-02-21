import jwt
import os
from dotenv import load_dotenv
from fastapi import Request, Response, status
from starlette.middleware.base import BaseHTTPMiddleware
from src.schemas.response import ErrorResponseSchema

load_dotenv()

HASHING_SECRET_KEY = os.getenv('HASHING_SECRET_KEY')
HASHING_ALGORITHM = os.getenv('HASHING_ALGORITHM')

class AuthenticationMiddleware(BaseHTTPMiddleware):
    def _unauthorized_response(message: str) -> Response:
        return Response(
            content=ErrorResponseSchema(message).json(),
            status_code=status.HTTP_401_UNAUTHORIZED,
            media_type="application/json",
        )
    
    async def dispatch(self, request: Request, call_next) -> Response:
        if not request.url.path.startswith('/user'):
            sent_token: str = request.headers.get('Authorization')

            if not sent_token:
                return self._unauthorized_response('Token não fornecido')

            if not sent_token.startswith('Bearer '):
                return self._unauthorized_response('Formato de token inválido. Use "Bearer <token>"')

            token_parts = sent_token.split(' ')

            if len(token_parts) != 2:
                return self._unauthorized_response('Formato de token inválido. Use "Bearer <token>"')

            token = token_parts[1]

            try:
                decoded_user = jwt.decode(token, HASHING_SECRET_KEY, algorithms=[HASHING_ALGORITHM])
                request.state.user = decoded_user
            except jwt.PyJWTError:
                return self._unauthorized_response('Token inválido ou expirado')

        response = await call_next(request)

        return response
