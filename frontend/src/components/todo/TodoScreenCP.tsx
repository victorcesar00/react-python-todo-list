import { JSX, useState, useEffect } from 'react'
import useAuth from "@/hooks/UseAuth";
import { useNavigate } from "react-router-dom"
import TodoService from "@/http/services/TodoService"
import ITodoResponseDTO from "@/http/dtos/response/ITodoResponseDTO"
import TodoListICP from "@/components/todo/inner/TodoListICP";
import RegisterTodoICP from '@/components/todo/inner/RegisterTodoICP';
import { isError } from '@/utils/ErrorHandlingUtils';

export default function TodoScreenCP(): JSX.Element {
    const [todos, setTodos] = useState<ITodoResponseDTO[]>()
    
    const { user, userIsLoading, logout } = useAuth()
    const navigate = useNavigate()
    
    useEffect(checkUserAuthentication, [user, userIsLoading, navigate])
    useEffect(getTodosEffect, [user])

    function checkUserAuthentication(): void {
        if(!userIsLoading && !user) {
            navigate('/')
        }
    }

    function getTodosEffect(): void {
        async function getTodos(): Promise<void> {
            if(user) {
                const response = await TodoService.getTodosByUserId(user.id)

                if(isError(response))
                    return

                setTodos(response)
            }
        }

        getTodos()
    }

    return (
        (userIsLoading || !user) ?
            <h1>Carregando...</h1>
            :
            <>
                <div style={{
                    width: 500,
                    display: 'flex',
                    alignItems: 'end',
                    justifyContent: 'space-between'
                }}>
                    <div>
                        <h3>Todo List</h3>
                        <RegisterTodoICP
                            user={user}
                            todos={todos}
                            setTodos={setTodos}
                        />
                    </div>
                    <button onClick={logout}>Sair</button>
                </div>

                <br/>
                <br/>

                <TodoListICP
                    user={user}
                    todos={todos}
                    setTodos={setTodos}
                />
            </>
            
    )
}