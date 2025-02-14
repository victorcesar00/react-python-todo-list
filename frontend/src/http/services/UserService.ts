import Api from "@/http/Api"
import ILoginRequest from "@/http/dtos/request/ILoginRequestDTO"
import IUserResponseDTO from "@/http/dtos/response/IUserResponseDTO"

export default class UserService {
    private static BASE_PATH = 'user'

    public static async login(credentials: ILoginRequest): Promise<IUserResponseDTO | unknown> {
        try {
            const user = await Api.post<IUserResponseDTO>(`${this.BASE_PATH}/login`, credentials)

            return user
        } catch(error) {
            return error
        }
    }

    public static async getUser(userId: number): Promise<IUserResponseDTO | unknown> {
        try {
            const user = await Api.get<IUserResponseDTO>(`${this.BASE_PATH}/${userId}`)

            return user
        } catch(error) {
            return error
        }
    }
}