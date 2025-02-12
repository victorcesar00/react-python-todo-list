import { JSX } from "react"

export default function LoginFormICP(): JSX.Element {
    return (
        <form>
            <h3>Login</h3>

            <input placeholder='Usuário'/>
            <br/>
            <input
                type='password'
                placeholder='Senha'
            />

            <br/>
            <br/>

            <button type='submit'>Entrar</button>
        </form>
    )
}