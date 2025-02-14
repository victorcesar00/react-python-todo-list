import { JSX, useState } from "react"
import { useNavigate } from "react-router-dom";
import ILoginRequestDTO from "@/http/dtos/request/ILoginRequestDTO"
import IUserResponseDTO from "@/http/dtos/response/IUserResponseDTO"
import UserService from "@/http/services/UserService"
import useAuth from "@/hooks/UseAuth"

interface IErrorLabelsFormat {
    usernameErrorLabel: string | undefined,
    passwordErrorLabel: string | undefined
    loginErrorLabel: string | undefined
}

const ERROR_LABELS_INITIAL_STATE: IErrorLabelsFormat = {
    usernameErrorLabel: undefined,
    passwordErrorLabel: undefined,
    loginErrorLabel: undefined
}

export default function LoginFormICP(): JSX.Element {
    const [errorLabels, setErrorLabels] = useState<IErrorLabelsFormat>(ERROR_LABELS_INITIAL_STATE)

    const { login } = useAuth()
    const navigate = useNavigate()

    async function handleSubmit(event: React.FormEvent<HTMLFormElement>): Promise<void> {
        event.preventDefault()

        const formData = new FormData(event.currentTarget)
        const credentials: ILoginRequestDTO = {
            username: formData.get('username') as string,
            password: formData.get('password') as string
        }

        const credentialsAreValid = validateCredentials(credentials)

        if(!credentialsAreValid)
            return

        const response = await UserService.login(credentials)

        if(response instanceof Error) {
            setErrorLabels({...ERROR_LABELS_INITIAL_STATE, loginErrorLabel: response.message})
            return
        }

        login(response as IUserResponseDTO)

        navigate('/todos')
    }

    function validateCredentials(credentials: ILoginRequestDTO): boolean {
        const newErrors: IErrorLabelsFormat = { ...ERROR_LABELS_INITIAL_STATE }
        
        switch(true) {
            case credentials.username === '':
                newErrors.usernameErrorLabel = 'Escreva um nome de usuário'
                break
            case /[^a-zA-Z0-9_]/.test(credentials.username):
                newErrors.usernameErrorLabel = 'Nome de usuário não contém caracteres especiais'
                break
            case credentials.username.length < 5:
                newErrors.usernameErrorLabel = 'Nome de usuário tem no mínimo 5 caracteres'
                break
        }

        switch(true) {
            case credentials.password === '':
                newErrors.passwordErrorLabel = 'Escreva sua senha'
                break
            case credentials.password.length < 5:
                newErrors.passwordErrorLabel = 'Senha tem no mínimo 5 caracteres'
                break
        }

        setErrorLabels(newErrors)

        const formIsValid = !newErrors.usernameErrorLabel && !newErrors.passwordErrorLabel

        return formIsValid
    }

    
    return (
        <form onSubmit={handleSubmit}>
            <h3>Login</h3>

            <input
                name='username'
                placeholder='Usuário'
            />
            
            <br/>
            <span style={{ color: 'red' }}>{errorLabels.usernameErrorLabel}</span>            
            <br/>

            <input
                name='password'
                type='password'
                placeholder='Senha'
            />

            <br/>

            <span style={{ color: 'red' }}>{errorLabels.passwordErrorLabel}</span>
            
            <br/>
            <span style={{ color: 'red' }}>{errorLabels.loginErrorLabel}</span>
            <br/>

            <button type='submit'>Entrar</button>
        </form>
    )
}