import Api from "@/http/Api"
import ILoginRequest from "@/http/dtos/request/ILoginRequestDTO"
import ITokenResponseDTO from "@/http/dtos/response/ITokenResponseDTO"

export default class UserService {
    private static BASE_PATH = 'user'

    public static async login(credentials: ILoginRequest): Promise<ITokenResponseDTO | Error> {
        try {
            return await Api.urlEncodedPost<ITokenResponseDTO>(`${this.BASE_PATH}/login`, credentials, false)
        } catch(error) {
            return error as Error
        }
    }

    public static async validateToken(): Promise<boolean | Error> {
        try {
            return await Api.get<boolean>(`${this.BASE_PATH}/validate-token`)
        } catch(error) {
            return error as Error
        }
    }
}