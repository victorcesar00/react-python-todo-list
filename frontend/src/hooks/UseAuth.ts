import { useEffect, useState } from "react"
import UserService from "@/http/services/UserService"
import IUserResponseDTO from "@/http/dtos/response/IUserResponseDTO"
import { isError } from "@/utils/ErrorHandlingUtils"

interface IReturnFormat {
    user: IUserResponseDTO | null
    login: (user: IUserResponseDTO) => void
    logout: () => void
    userIsLoading: boolean
}

export default function useAuth(): IReturnFormat {
    const [user, setUser] = useState<IUserResponseDTO | null>(null)
    const [userIsLoading, setUserIsLoading] = useState(true)

    useEffect(() => {
        const getUser = async () => {
            const userIdOnLocalStorage = localStorage.getItem('userId')

            if(!userIdOnLocalStorage) {
                setUser(null)
                return
            }

            const response = await UserService.getUser(Number(userIdOnLocalStorage))

            if(isError(response)) {
                localStorage.removeItem('userId')

                setUser(null)
                return
            }

            setUser(response)
        }

        getUser().then(() => setUserIsLoading(false))
    }, [])

    const login = (user: IUserResponseDTO): void => {
        localStorage.setItem('userId', user.id.toString())
        setUser(user)
    }

    const logout = (): void => {
        localStorage.removeItem('userId')
        setUser(null)
    }

    return { user, login, logout, userIsLoading }

}

