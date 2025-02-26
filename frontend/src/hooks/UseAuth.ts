import { useEffect, useState } from "react"
import UserService from "@/http/services/UserService"
import { isError } from "@/utils/ErrorHandlingUtils"
import { getSavedToken, removeSavedToken, saveToken } from "@/utils/AuthenticationUtils"
import ILoginRequestDTO from "@/http/dtos/request/ILoginRequestDTO"

interface IReturnFormat {
    userIsAuthenticated: boolean
    login: (user: ILoginRequestDTO) => Promise<string | Error>
    logout: () => void
    authIsLoading: boolean
}

export default function useAuth(): IReturnFormat {
    const [userIsAuthenticated, setUserIsAuthenticated] = useState(false)
    const [authIsLoading, setAuthIsLoading] = useState(true)

    useEffect(getTokenEffect, [])

    function getTokenEffect(): void {
        const getToken = async () => {
            const savedToken = getSavedToken()

            if(!savedToken)
                return

            const response = await UserService.validateToken()

            if(isError(response)) {
                removeSavedToken()

                return
            }

            setUserIsAuthenticated(true)
        }

        getToken().then(() => setAuthIsLoading(false))
    }

    const login = async (credentials: ILoginRequestDTO): Promise<string | Error> => {
        setAuthIsLoading(true)

        const response = await UserService.login(credentials)

        if(isError(response)) {
            setUserIsAuthenticated(false)
            setAuthIsLoading(false)

            return response
        }
        
        saveToken(response.access_token)

        setUserIsAuthenticated(true)
        setAuthIsLoading(false)

        return response.access_token
    }

    const logout = (): void => {
        removeSavedToken()
        setUserIsAuthenticated(false)
    }

    return { userIsAuthenticated, login, logout, authIsLoading }

}

