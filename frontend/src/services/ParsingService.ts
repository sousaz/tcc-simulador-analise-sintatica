// @ts-ignore
import api from '../utils/Api';

export async function getAllData(grammar: string, input: string, analysisType: string): Promise<any> {
    return await api.get(`/analyze/${grammar}/${input}/${analysisType}`);
};

/* 
export async function heavyLoad() {
    const request = new Promise((resolve, handleError) => {
        setInterval(() => {
            resolve(true);
        }, 3000)
    })
}
*/