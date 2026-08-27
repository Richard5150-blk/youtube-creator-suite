import React from 'react';

const Login: React.FC = () => {
  return (
    <div className="min-h-screen bg-dark-900 flex items-center justify-center p-4">
      <div className="bg-dark-800 rounded-lg border border-dark-700 p-8 w-full max-w-md">
        <h1 className="text-2xl font-bold text-primary-500 mb-6 text-center">YouTube Creator Suite</h1>
        <button className="w-full btn-primary mb-4">Sign in with Google</button>
        <p className="text-center text-dark-400 text-sm">Connect your YouTube channel to get started</p>
      </div>
    </div>
  );
};

export default Login;
