import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Bars3Icon, XMarkIcon } from '@heroicons/react/24/outline';
import {
  SparklesIcon,
  ChartBarIcon,
  VideoCameraIcon,
  PhotoIcon,
  SpeakerWaveIcon,
  FilmIcon,
} from '@heroicons/react/24/solid';

interface SidebarProps {
  isOpen: boolean;
  onToggle: () => void;
}

const Sidebar: React.FC<SidebarProps> = ({ isOpen, onToggle }) => {
  const location = useLocation();

  const navItems = [
    { path: '/', label: 'Dashboard', icon: SparklesIcon },
    { path: '/analytics', label: 'Analytics', icon: ChartBarIcon },
    { path: '/videos/generate', label: 'Generate Videos', icon: VideoCameraIcon },
    { path: '/thumbnails', label: 'Thumbnails', icon: PhotoIcon },
    { path: '/voice', label: 'Voice', icon: SpeakerWaveIcon },
    { path: '/render', label: 'Render', icon: FilmIcon },
  ];

  return (
    <>
      {/* Mobile Toggle Button */}
      <button
        onClick={onToggle}
        className="fixed top-4 left-4 z-50 md:hidden p-2 rounded-lg bg-dark-800 text-dark-50"
      >
        {isOpen ? (
          <XMarkIcon className="w-6 h-6" />
        ) : (
          <Bars3Icon className="w-6 h-6" />
        )}
      </button>

      {/* Sidebar */}
      <aside
        className={`${
          isOpen ? 'translate-x-0' : '-translate-x-full'
        } fixed md:relative w-64 h-screen bg-dark-800 border-r border-dark-700 transition-transform duration-300 z-40 overflow-y-auto`}
      >
        {/* Logo */}
        <div className="p-6 border-b border-dark-700">
          <h1 className="text-2xl font-bold text-primary-500">YCS</h1>
          <p className="text-xs text-dark-400">YouTube Creator Suite</p>
        </div>

        {/* Navigation */}
        <nav className="p-4 space-y-2">
          {navItems.map((item) => {
            const Icon = item.icon;
            const isActive = location.pathname === item.path;
            return (
              <Link
                key={item.path}
                to={item.path}
                className={`flex items-center space-x-3 px-4 py-3 rounded-lg transition-colors ${
                  isActive
                    ? 'bg-primary-500 text-white'
                    : 'text-dark-300 hover:bg-dark-700'
                }`}
              >
                <Icon className="w-5 h-5" />
                <span className="text-sm font-medium">{item.label}</span>
              </Link>
            );
          })}
        </nav>
      </aside>

      {/* Mobile Overlay */}
      {isOpen && (
        <div
          className="fixed inset-0 bg-black/50 md:hidden z-30"
          onClick={onToggle}
        />
      )}
    </>
  );
};

export default Sidebar;
