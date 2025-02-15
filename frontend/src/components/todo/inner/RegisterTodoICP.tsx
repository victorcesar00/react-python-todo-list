import { JSX, useContext, useRef } from 'react'
import TodoService from "@/http/services/TodoService"
import ICreateTodoRequestDTO from '@/http/dtos/request/ICreateTodoRequestDTO'
import { isError } from '@/utils/ErrorHandlingUtils'
import TodoContext, { ITodoContextFormat } from '@/context/TodoContext'

export default function RegisterTodoICP(): JSX.Element {
    const inputRef = useRef<HTMLInputElement>(null)

    const todoContext = useContext<ITodoContextFormat>(TodoContext)
    
    async function confirm(newTodo: string): Promise<void> {
        if(!todoContext.todos)
            return

        const payload: ICreateTodoRequestDTO = {
            user_id: todoContext.user.id,
            description: newTodo
        }

        const response = await TodoService.createTodo(payload)

        if(isError(response))
            return

        todoContext.setTodos([ ...todoContext.todos, response ])

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