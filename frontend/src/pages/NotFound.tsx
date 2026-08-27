import React from 'react';
import { useNavigate } from 'react-router-dom';

const NotFound: React.FC = () => {
  const navigate = useNavigate();

  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      <h1 className="text-4xl font-bold text-dark-50 mb-2">404</h1>
      <p className="text-dark-400 mb-6">Page not found</p>
      <button
        onClick={() => navigate('/')}
        className="btn-primary"
      >
        Back to Dashboard
      </button>
    </div>
  );
};

export default NotFound;
