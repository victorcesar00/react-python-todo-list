import Api from "@/http/Api"
import ITodoResponseDTO from "@/http/dtos/response/ITodoResponseDTO"
import ICreateTodoRequestDTO from "@/http/dtos/request/ICreateTodoRequestDTO"

export default class TodoService {
    private static BASE_PATH = 'todo'

    public static async getUserTodos(): Promise<ITodoResponseDTO[] | Error> {
        try {
            return await Api.get<ITodoResponseDTO[]>(`${this.BASE_PATH}/user`)
        } catch(error) {
            alert('Erro ao tentar buscar tarefas')

            return error as Error
        }
    }

    public static async createTodo(payload: ICreateTodoRequestDTO): Promise<ITodoResponseDTO | Error> {
        try {
            return await Api.post<ITodoResponseDTO>(`${this.BASE_PATH}`, payload)
        } catch(error) {
            alert('Erro ao criar tarefa')

            return error as Error
        }
    }

    public static async editTodo(updatedTodo: ITodoResponseDTO): Promise<ITodoResponseDTO | Error> {
        try {
            return await Api.put<ITodoResponseDTO>(`${this.BASE_PATH}`, updatedTodo)
        } catch(error) {
            alert('Erro ao editar tarefa')

            return error as Error
        }
        
    }

    public static async deleteTodo(todoId: number): Promise<boolean | Error> {
        try {
            return await Api.delete<boolean>(`${this.BASE_PATH}/${todoId}`)
        } catch(error) {
            alert('Erro ao deletar tarefa')

            return error as Error
        }
        
    }
}