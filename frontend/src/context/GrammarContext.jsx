import { createContext, useContext, useState } from 'react'

const GrammarContext = createContext()

export default function GrammarProvider({ children }) {
    const [grammar, setGrammar] = useState("S->id.")
    return (
        <GrammarContext.Provider value={{ grammar, setGrammar }}>
            {children}
        </GrammarContext.Provider>
    )
}

export const useGrammar = () => useContext(GrammarContext)