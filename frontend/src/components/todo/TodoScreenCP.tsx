import { JSX, useState, useEffect } from 'react'
import useAuth from "@/hooks/UseAuth"
import { useNavigate } from "react-router-dom"
import TodoService from "@/http/services/TodoService"
import TodoListICP from "@/components/todo/inner/TodoListICP"
import ITodoResponseDTO from "@/http/dtos/response/ITodoResponseDTO"
import RegisterTodoICP from '@/components/todo/inner/RegisterTodoICP'
import { isError } from '@/utils/ErrorHandlingUtils'
import TodoContext from '@/context/TodoContext'


export default function TodoScreenCP(): JSX.Element {
    const [todos, setTodos] = useState<ITodoResponseDTO[]>()
    
    const { userIsAuthenticated, authIsLoading, logout } = useAuth()
    const navigate = useNavigate()
    
    useEffect(checkUserAuthentication, [userIsAuthenticated, authIsLoading, navigate])

    function checkUserAuthentication(): void {
        if(!authIsLoading) {
            if(!userIsAuthenticated) {
                navigate('/')
    
                return
            }

            getTodos()
        }
    }

    function getTodos(): void {
        async function getTodos(): Promise<void> {
            const response = await TodoService.getUserTodos()

            if(isError(response))
                return

            setTodos(response)
        }

        getTodos()
    }

    return (
        authIsLoading ?
            <h1>Carregando...</h1>
            :
            <TodoContext.Provider value={{ todos, setTodos }}>
                <div style={{
                    width: 500,
                    display: 'flex',
                    alignItems: 'end',
                    justifyContent: 'space-between'
                }}>
                    <div>
                        <h3>Todo List</h3>
                        <RegisterTodoICP/>
                    </div>
                    <button onClick={logout}>Sair</button>
                </div>

                <br/>
                <br/>

                <TodoListICP/>
            </TodoContext.Provider>
            
    )
}