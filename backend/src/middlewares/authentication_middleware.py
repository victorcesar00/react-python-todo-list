import jwt
import os
import json
from fastapi import Request, Response, status
from dotenv import load_dotenv
from starlette.middleware.base import BaseHTTPMiddleware
from src.schemas.response import ErrorResponseSchema

load_dotenv()

HASHING_SECRET_KEY = os.getenv('HASHING_SECRET_KEY')
HASHING_ALGORITHM = os.getenv('HASHING_ALGORITHM')

class AuthenticationMiddleware(BaseHTTPMiddleware):
    @staticmethod
    def _unauthorized_response(message: str) -> Response:
        return Response(
            content=ErrorResponseSchema(message = message).json(),
            status_code=status.HTTP_401_UNAUTHORIZED,
            media_type="application/json",
        )
    
    async def dispatch(self, request: Request, call_next) -> Response:
        if request.url.path.startswith('/todo') or request.url.path.startswith('/todo/validate-token'):
            sent_token: str = request.headers.get('Authorization')

            if not sent_token:
                return self._unauthorized_response('Token not provided')

            if not sent_token.startswith('Bearer '):
                return self._unauthorized_response('Invalid token format. Use "Bearer <token>"')

            token_parts = sent_token.split(' ')

            if len(token_parts) != 2:
                return self._unauthorized_response('Invalid token format. Use "Bearer <token>"')

            token = token_parts[1]

            try:
                decoded_token = jwt.decode(token, HASHING_SECRET_KEY, algorithms=[HASHING_ALGORITHM])
                request.scope['user'] = json.loads(decoded_token['sub'])
            except jwt.PyJWTError:
                return self._unauthorized_response('Invalid or expired token')

        response = await call_next(request)

        return response
