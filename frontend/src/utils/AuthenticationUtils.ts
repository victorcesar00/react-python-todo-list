export function getSavedToken(): string | null {
    return localStorage.getItem('user-jwt')
}

export function removeSavedToken(): void {
    localStorage.removeItem('user-jwt')
}

export function saveToken(token: string): void {
    localStorage.setItem('user-jwt', token)
}