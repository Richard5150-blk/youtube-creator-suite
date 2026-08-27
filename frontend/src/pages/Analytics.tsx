import React from 'react';
import { ChartBarIcon } from '@heroicons/react/24/solid';

const Analytics: React.FC = () => {
  return (
    <div className="space-y-6">
      <div className="flex items-center space-x-3">
        <ChartBarIcon className="w-8 h-8 text-primary-500" />
        <h1 className="text-2xl md:text-3xl font-bold text-dark-50">Analytics</h1>
      </div>

      <div className="grid grid-cols-1 gap-4">
        <div className="bg-dark-800 rounded-lg border border-dark-700 p-6">
          <h2 className="text-lg font-semibold text-dark-50 mb-4">Channel Performance</h2>
          <p className="text-dark-400">Analytics data will be displayed here</p>
        </div>
      </div>
    </div>
  );
};

export default Analytics;
