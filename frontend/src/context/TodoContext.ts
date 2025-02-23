import { createContext } from 'react'
import ITodoResponseDTO from "@/http/dtos/response/ITodoResponseDTO"

export interface ITodoContextFormat {
    todos?: ITodoResponseDTO[]
    setTodos: (todos: ITodoResponseDTO[]) => void
}

const INITIAL_STATE: ITodoContextFormat = {
    setTodos: () => {}
}

const TodoContext = createContext<ITodoContextFormat>(INITIAL_STATE)

export default TodoContext