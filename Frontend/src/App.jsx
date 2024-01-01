import React from 'react'
import { Route, Router, Routes } from 'react-router-dom'
const App = () => {
  return (
    <div className='flex h-screen'>
      <Routes>
        <Route path='/' element = {<Home/>}/>
      </Routes>
    </div>
  )
}

export default App