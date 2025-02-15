import { JSX } from 'react'
import ITodoResponseDTO from "@/http/dtos/response/ITodoResponseDTO"
import TodoICP from "@/components/todo/inner/TodoICP"
import IUserResponseDTO from '@/http/dtos/response/IUserResponseDTO'

interface ITodoListICPPropsFormat {
    user: IUserResponseDTO
    todos?: ITodoResponseDTO[]
    setTodos: (todos: ITodoResponseDTO[]) => void
}

export default function TodoListICP(props: ITodoListICPPropsFormat): JSX.Element {
    function updateTodoOnList(updatedTodo: ITodoResponseDTO): void {
        if(!props.todos)
            return
        
        const updatedList = props.todos.map(todo => {
            if(todo.id === updatedTodo.id)
                return updatedTodo

            return todo
        })

        props.setTodos(updatedList)
    }

    function removeTodoFromList(todoIdToDelete: number): void {
        if(!props.todos)
            return

        const todosCopy = [ ...props.todos ]

        const todosWithoutRemoved = todosCopy.filter(todo => todo.id !== todoIdToDelete)

        props.setTodos(todosWithoutRemoved)
    }

    return (
        <>
            {props.todos ?
                props.todos.map((todo) => (
                    <TodoICP
                        key={todo.id}
                        todo={todo}
                        updateTodoOnList={updateTodoOnList}
                        removeTodoFromList={removeTodoFromList}
                    />
                ))
                : <h1>Carregando...</h1>
            }
        </>
    )
}