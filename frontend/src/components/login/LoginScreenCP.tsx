import { JSX, useEffect } from "react"
import LoginFormICP from "./inner/LoginFormICP"
import useAuth from "@/hooks/UseAuth"
import { useNavigate } from "react-router-dom"
import LoadingCP from "@/components/common/LoadingCP"

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
            <LoadingCP/>
            : <>
                <h3>Login</h3>
                <LoginFormICP/>
            </> 
    )
}