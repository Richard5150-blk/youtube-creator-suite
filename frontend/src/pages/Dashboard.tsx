import React from 'react';
import { SparklesIcon } from '@heroicons/react/24/solid';
import Loading from '@/components/Loading';

const Dashboard: React.FC = () => {
  const [stats] = React.useState([
    { label: 'Total Videos', value: '24', trend: '+12%' },
    { label: 'Total Views', value: '150K', trend: '+25%' },
    { label: 'Subscribers', value: '5.2K', trend: '+8%' },
    { label: 'Avg. Watch Time', value: '4:32', trend: '+15%' },
  ]);

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center space-x-3">
        <SparklesIcon className="w-8 h-8 text-primary-500" />
        <h1 className="text-2xl md:text-3xl font-bold text-dark-50">Dashboard</h1>
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {stats.map((stat, index) => (
          <div
            key={index}
            className="bg-dark-800 rounded-lg p-4 md:p-6 border border-dark-700 hover:border-primary-500 transition-colors"
          >
            <p className="text-dark-400 text-sm mb-2">{stat.label}</p>
            <p className="text-2xl md:text-3xl font-bold text-dark-50 mb-2">{stat.value}</p>
            <p className="text-xs text-green-400">{stat.trend} from last month</p>
          </div>
        ))}
      </div>

      {/* Quick Actions */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <button className="bg-primary-500 hover:bg-primary-600 text-white font-semibold py-3 px-6 rounded-lg transition-colors w-full">
          Generate Long-Form Video
        </button>
        <button className="bg-primary-500 hover:bg-primary-600 text-white font-semibold py-3 px-6 rounded-lg transition-colors w-full">
          Generate Short-Form Video
        </button>
      </div>

      {/* Recent Activity */}
      <div className="bg-dark-800 rounded-lg border border-dark-700 p-4 md:p-6">
        <h2 className="text-lg font-semibold text-dark-50 mb-4">Recent Activity</h2>
        <div className="space-y-3">
          {[1, 2, 3].map((i) => (
            <div key={i} className="flex items-center justify-between p-3 bg-dark-700 rounded-lg">
              <div>
                <p className="text-dark-50 font-medium">Video #".{i} Generated</p>
                <p className="text-dark-400 text-sm">2 hours ago</p>
              </div>
              <span className="px-3 py-1 bg-green-500/20 text-green-400 text-xs rounded-full">Completed</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
