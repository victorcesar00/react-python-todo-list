import { JSX, useRef } from 'react'
import TodoService from "@/http/services/TodoService"
import IUserResponseDTO from '@/http/dtos/response/IUserResponseDTO'
import ICreateTodoRequestDTO from '@/http/dtos/request/ICreateTodoRequestDTO'
import ITodoResponseDTO from "@/http/dtos/response/ITodoResponseDTO"
import { isError } from '@/utils/ErrorHandlingUtils'

interface IRegisterTodoICPPropsFormat {
    user: IUserResponseDTO
    todos?: ITodoResponseDTO[]
    setTodos: (todos: ITodoResponseDTO[]) => void
}

export default function RegisterTodoICP(props: IRegisterTodoICPPropsFormat): JSX.Element {
    const inputRef = useRef<HTMLInputElement>(null)
    
    async function confirm(newTodo: string): Promise<void> {
        if(!props.todos)
            return

        const payload: ICreateTodoRequestDTO = {
            user_id: props.user.id,
            description: newTodo
        }

        const response = await TodoService.createTodo(payload)

        if(isError(response))
            return

        props.setTodos([ ...props.todos, response ])

        cleanInput()
    }

    function handleSubmit(): void {
        const newTodo = inputRef.current?.value

        if(!newTodo || newTodo.trim() === '')
            return

        confirm(newTodo)
    }

    function cleanInput(): void {
        if(inputRef.current)
            inputRef.current.value = ''
    }

    function handleKeyDown(event: React.KeyboardEvent<HTMLInputElement>): void {
        if(event.key === 'Enter')
            handleSubmit()
    }

    return (
        <>
            <input
                placeholder="Todo"
                ref={inputRef}
                onKeyDown={handleKeyDown}
            />
            {' '}
            <button onClick={handleSubmit}>Salvar</button>
        </>
    )
}