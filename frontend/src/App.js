import React, { useState } from 'react';
     import './App.css';

     function App() {
       const [condition, setCondition] = useState('');
       const [response, setResponse] = useState(null);
       const [error, setError] = useState('');

       const handleSubmit = async (e) => {
         e.preventDefault();
         setError('');
         setResponse(null);
         try {
           const res = await fetch('http://127.0.0.1:5000/health-plan', {
             method: 'POST',
             headers: { 'Content-Type': 'application/json' },
             body: JSON.stringify({ condition })
           });
           const data = await res.json();
           if (res.ok) {
             setResponse(data);
           } else {
             setError(data.error || 'Failed to fetch health plan');
           }
         } catch (err) {
           setError('Error connecting to the API: ' + err.message);
         }
       };

       return (
         <div className="container mx-auto p-4">
           <h1 className="text-3xl font-bold mb-4">YogaCure</h1>
           <p className="mb-4">Enter a health condition to get personalized yoga and diet recommendations.</p>
           <form onSubmit={handleSubmit} className="mb-4">
             <input
               type="text"
               value={condition}
               onChange={(e) => setCondition(e.target.value)}
               placeholder="e.g., back pain, stress, diabetes"
               className="border p-2 mr-2 rounded"
             />
             <button type="submit" className="bg-blue-500 text-white p-2 rounded hover:bg-blue-600">Get Plan</button>
           </form>
           {error && <p className="text-red-500">{error}</p>}
           {response && (
             <div>
               <h2 className="text-2xl font-semibold mb-2">Plan for {response.condition}</h2>
               <h3 className="text-xl font-medium mt-4">Yoga Poses</h3>
               {response.yoga_plan.map((pose) => (
                 <div key={pose.id} className="border p-4 my-2 rounded shadow">
                   <p><strong>{pose.pose_name}</strong>: {pose.description}</p>
                   <p>Duration: {pose.duration_seconds} seconds</p>
                   <a href={pose.video_url} target="_blank" rel="noopener noreferrer" className="text-blue-500 hover:underline">Watch Video</a>
                 </div>
               ))}
               <h3 className="text-xl font-medium mt-4">Diet Plan</h3>
               {response.diet_plan.map((diet) => (
                 <div key={`${diet.day}-${diet.meal_type}`} className="border p-4 my-2 rounded shadow">
                   <p><strong>Day {diet.day} - {diet.meal_type}</strong>: {diet.meal_description}</p>
                 </div>
               ))}
             </div>
           )}
         </div>
       );
     }

     export default App;