import { JSX } from "react"
import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import LoginScreenCP from '@/components/login/LoginScreenCP'

import TodoScreenCP from "@/components/todo/TodoScreenCP"

function App(): JSX.Element {
  return (
    <Router>
      <Routes>
        <Route path='/' element={<LoginScreenCP/>}/>
        <Route path='/todos' element={<TodoScreenCP/>}/>
        <Route path='*' element={<LoginScreenCP/>}/>
        <Route/>
      </Routes>
    </Router>
  )
}

export default App
