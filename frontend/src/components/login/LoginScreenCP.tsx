import { JSX, useEffect } from "react"
import LoginFormICP from "./inner/LoginFormICP"
import useAuth from "@/hooks/UseAuth";
import { useNavigate } from "react-router-dom"

export default function LoginScreenCP(): JSX.Element {
    const { user, userIsLoading } = useAuth()
    const navigate = useNavigate()

    useEffect(checkUserAuthentication, [user, userIsLoading, navigate])

    function checkUserAuthentication() {
        if(!userIsLoading && user) {
            navigate('/todos')
        }
    }

    return (
        userIsLoading ?
            <h1>Carregando...</h1>
            : <LoginFormICP/>
    )
}