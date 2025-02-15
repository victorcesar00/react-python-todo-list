import { JSX, useContext } from 'react'
import ITodoResponseDTO from "@/http/dtos/response/ITodoResponseDTO"
import TodoICP from "@/components/todo/inner/TodoICP"
import TodoContext, { ITodoContextFormat } from '@/context/TodoContext'

export default function TodoListICP(): JSX.Element {
    const todoContext = useContext<ITodoContextFormat>(TodoContext)

    function updateTodoOnList(updatedTodo: ITodoResponseDTO): void {
        if(!todoContext.todos)
            return
        
        const updatedList = todoContext.todos.map(todo => {
            if(todo.id === updatedTodo.id)
                return updatedTodo

            return todo
        })

        todoContext.setTodos(updatedList)
    }

    function removeTodoFromList(todoIdToDelete: number): void {
        if(!todoContext.todos)
            return

        const todosCopy = [ ...todoContext.todos ]

        const todosWithoutRemoved = todosCopy.filter(todo => todo.id !== todoIdToDelete)

        todoContext.setTodos(todosWithoutRemoved)
    }

    return (
        <>
            {todoContext.todos ?
                todoContext.todos.map((todo) => (
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