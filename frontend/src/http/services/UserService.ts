import Api from "@/http/Api"
import ILoginRequest from "@/http/dtos/request/ILoginRequestDTO"
import IUserResponseDTO from "@/http/dtos/response/IUserResponseDTO"

export default class UserService {
    private static BASE_PATH = 'user'

    public static async login(credentials: ILoginRequest): Promise<IUserResponseDTO | Error> {
        try {
            return await Api.post<IUserResponseDTO>(`${this.BASE_PATH}/login`, credentials)
        } catch(error) {
            return error as Error
        }
    }

    public static async getUser(userId: number): Promise<IUserResponseDTO | Error> {
        try {
            return await Api.get<IUserResponseDTO>(`${this.BASE_PATH}/${userId}`)
        } catch(error) {
            return error as Error
        }
    }
}