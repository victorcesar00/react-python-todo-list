import ITodoResponseDTO from '@/http/dtos/response/ITodoResponseDTO'

export default interface IUserResponseDTO {
    id: number
    username: string
    todos: ITodoResponseDTO[]
}