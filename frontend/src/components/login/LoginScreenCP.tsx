import { JSX, useEffect } from "react"
import LoginFormICP from "./inner/LoginFormICP"
import useAuth from "@/hooks/UseAuth"
import { useNavigate } from "react-router-dom"

export default function LoginScreenCP(): JSX.Element {
    const { userIsAuthenticated, authIsLoading } = useAuth()
    const navigate = useNavigate()

    useEffect(checkUserAuthentication, [userIsAuthenticated, authIsLoading, navigate])

    function checkUserAuthentication() {
        if(!authIsLoading && userIsAuthenticated) {
            navigate('/todos')
        }
    }

    return (
        authIsLoading ?
            <h1>Carregando...</h1>
            : <>
                <h3>Login</h3>
                <LoginFormICP/>
            </> 
    )
}