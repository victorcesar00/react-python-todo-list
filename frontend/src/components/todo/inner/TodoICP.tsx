import { JSX, useRef, useState } from 'react'
import TodoService from '@/http/services/TodoService';
import ITodoResponseDTO from '@/http/dtos/response/ITodoResponseDTO';
import { isError } from '@/utils/ErrorHandlingUtils';

interface ITodoICPPropsFormat {
    todo: ITodoResponseDTO
    updateTodoOnList: (updatedTodo: ITodoResponseDTO) => void
    removeTodoFromList: (todoIdToDelete: number) => void
}

export default function TodoICP(props: ITodoICPPropsFormat): JSX.Element {
    const [isEditing, setIsEditing] = useState<boolean>(false)

    const inputRef = useRef<HTMLInputElement>(null)

    async function confirmEdit(): Promise<void> {
        const newDescription = inputRef.current?.value
        
        if(!newDescription || newDescription.trim() === '') {
            deleteTodo()
            return
        }

        const response = await TodoService.editTodo({ ...props.todo, description: newDescription })

        if(isError(response))
            return

        props.updateTodoOnList(response)

        setIsEditing(false)
    }

    async function deleteTodo(): Promise<void> {
        const response = await TodoService.deleteTodo(props.todo.id)

        if(isError(response))
            return

        props.removeTodoFromList(props.todo.id)
    }

    function handleKeyDown(event: React.KeyboardEvent<HTMLInputElement>): void {
        if(event.key === 'Enter')
            confirmEdit()

        if(event.key === 'Escape')
            setIsEditing(false)
    }

    return (
        <div style={{
            width: 500,
            borderBottom: '1px solid',
            paddingBottom: 10
        }}>
            <h4>
                {isEditing ?
                    <>
                        <input
                            defaultValue={props.todo.description}
                            ref={inputRef}
                            onKeyDown={handleKeyDown}
                        />
                        {' '}
                        <button onClick={confirmEdit}>Confirmar</button>
                    </>
                    : props.todo.description
                }
            </h4>

            {!isEditing &&
                <>
                    <button onClick={() => setIsEditing(true)}>Editar</button>
                    {' '}
                    <button onClick={() => deleteTodo()}>Excluir</button>
                </>
            }
        </div>
    )
}