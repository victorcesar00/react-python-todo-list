export function isError(response: unknown): response is Error {
    return response instanceof Error
}