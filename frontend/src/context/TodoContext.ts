import { createContext } from 'react'
import ITodoResponseDTO from "@/http/dtos/response/ITodoResponseDTO"
import IUserResponseDTO from '@/http/dtos/response/IUserResponseDTO'

export interface ITodoContextFormat {
    user: IUserResponseDTO
    todos?: ITodoResponseDTO[]
    setTodos: (todos: ITodoResponseDTO[]) => void
}

const INITIAL_STATE: ITodoContextFormat = {
    user: {} as IUserResponseDTO,
    setTodos: () => {}
}

const TodoContext = createContext<ITodoContextFormat>(INITIAL_STATE)

export default TodoContext