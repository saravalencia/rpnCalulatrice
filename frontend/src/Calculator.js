import axios from 'axios';
import React, { useState } from 'react';

const Calculator = () => {
    const [expression, setExpression] = useState('');
    const [result, setResult] = useState('');

    const handleCalculate = async () => {
        try {
            const response = await axios.post('http://localhost:8000/calculate', { expression });
            setResult(response.data.result);
        } catch (error) {
            console.error('Error during API call', error);

        }
    };

    return (
        <div>
            <input type="text" value={expression} onChange={(e) => setExpression(e.target.value)} />
            <button onClick={handleCalculate} >Calculate</button>
            <p>Result:{result}</p>
        </div>
    );
};

export default Calculator;
