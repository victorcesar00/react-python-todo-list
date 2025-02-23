import { removeSavedToken } from "@/utils/AuthenticationUtils"

export default class Api {
    private static BASE_URL = 'api/'

    private static DEFAULT_HEADERS = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    private static async request<T>(endpoint: string, options: RequestInit, authenticated: boolean): Promise<T> {
        const optionsCopy = { ...options }

        if(authenticated) {
            optionsCopy.headers = {
                ...this.DEFAULT_HEADERS,
                'Authorization': `Bearer ${localStorage.getItem('user-jwt')}`
            }
        }

        const response = await fetch(`${this.BASE_URL}${endpoint}`, optionsCopy)

        return this.handleResponse<T>(response, authenticated)
    }

    private static async handleResponse<T>(response: Response, authenticated: boolean): Promise<T> {
        const jsonBodyResponse = await response.json()
        
        if (!response.ok) {
            if(authenticated && response.status === 401) {
                alert('Usuário não autenticado')

                removeSavedToken()

                window.location.href = '/login'
            }

            if(jsonBodyResponse.message) {
                throw new Error(`Erro: ${jsonBodyResponse.message}`)
            }
    
            throw new Error(`Erro ${response.status}: ${response.statusText}`)
        }

        return jsonBodyResponse as T
    }

    public static get<T>(endpoint: string, authenticated = true): Promise<T> {
        return this.request<T>(endpoint, { method: 'GET' }, authenticated)
    }

    public static post<T>(endpoint: string, body: unknown, authenticated = true): Promise<T> {
        return this.request<T>(endpoint, {
            method: 'POST',
            headers: this.DEFAULT_HEADERS,
            body: JSON.stringify(body)
        }, authenticated)
    }

    public static urlEncodedPost<T>(endpoint: string, body: object, authenticated = true): Promise<T> {
        const urlEncodedData = new URLSearchParams(body as Record<string, string>).toString()
        
        return this.request<T>(endpoint, {
            method: 'POST',
            headers: { ...this.DEFAULT_HEADERS, 'Content-Type': 'application/x-www-form-urlencoded' },
            body: urlEncodedData
        }, authenticated)
    }

    public static put<T>(endpoint: string, body: object, authenticated = true): Promise<T> {
        return this.request<T>(endpoint, {
            method: 'PUT',
            headers: this.DEFAULT_HEADERS,
            body: JSON.stringify(body)
        }, authenticated)
    }

    public static delete<T>(endpoint: string, authenticated = true): Promise<T> {
        return this.request<T>(endpoint, { method: 'DELETE' }, authenticated)
    }
}
