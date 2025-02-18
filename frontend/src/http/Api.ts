export default class Api {
    private static BASE_URL = "api/"

    private static DEFAULT_HEADERS = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    private static async request<T>(endpoint: string, options: RequestInit): Promise<T> {
        const response = await fetch(`${this.BASE_URL}${endpoint}`, options)

        return this.handleResponse<T>(response)
    }

    private static async handleResponse<T>(response: Response): Promise<T> {
        if (!response.ok) {
            const jsonResponse = (await response.json())

            if(jsonResponse.message) {
                throw new Error(`Erro: ${jsonResponse.message}`)
            }
    
            throw new Error(`Erro ${response.status}: ${response.statusText}`, jsonResponse.detail)
        }

        return response.json() as Promise<T>
    }

    public static get<T>(endpoint: string): Promise<T> {
        return this.request<T>(endpoint, { method: 'GET' })
    }

    public static post<T>(endpoint: string, body: unknown): Promise<T> {
        return this.request<T>(endpoint, {
            method: 'POST',
            headers: this.DEFAULT_HEADERS,
            body: JSON.stringify(body),
        })
    }

    public static put<T>(endpoint: string, body: unknown): Promise<T> {
        return this.request<T>(endpoint, {
            method: 'PUT',
            headers: this.DEFAULT_HEADERS,
            body: JSON.stringify(body),
        })
    }

    public static delete<T>(endpoint: string): Promise<T> {
        return this.request<T>(endpoint, { method: 'DELETE' })
    }
}
