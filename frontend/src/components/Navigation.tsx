import React from 'react';
import { UserCircleIcon, Cog6ToothIcon, ArrowLeftOnRectangleIcon } from '@heroicons/react/24/outline';

const Navigation: React.FC = () => {
  return (
    <nav className="bg-dark-800 border-b border-dark-700 px-4 md:px-6 py-4 flex items-center justify-between">
      <div className="flex items-center space-x-2">
        <h2 className="text-lg font-semibold text-dark-50">YouTube Creator Suite</h2>
      </div>

      <div className="flex items-center space-x-4">
        <button className="p-2 rounded-lg hover:bg-dark-700 transition-colors">
          <Cog6ToothIcon className="w-5 h-5 text-dark-400" />
        </button>
        <button className="p-2 rounded-lg hover:bg-dark-700 transition-colors">
          <UserCircleIcon className="w-5 h-5 text-dark-400" />
        </button>
        <button className="p-2 rounded-lg hover:bg-dark-700 transition-colors">
          <ArrowLeftOnRectangleIcon className="w-5 h-5 text-dark-400" />
        </button>
      </div>
    </nav>
  );
};

export default Navigation;
