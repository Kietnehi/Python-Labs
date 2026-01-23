'use client';

import React, { useState, useEffect } from 'react';
import { Search, Image as ImageIcon, Video, Book, Newspaper, LayoutGrid, Globe, PlayCircle, Calendar, User, Moon, Sun } from 'lucide-react';

// Định nghĩa các loại kết quả tìm kiếm
const TABS = [
  { id: 'text', label: 'Tất cả', icon: <Globe size={18} /> },
  { id: 'news', label: 'Tin tức', icon: <Newspaper size={18} /> },
  { id: 'images', label: 'Hình ảnh', icon: <ImageIcon size={18} /> },
  { id: 'videos', label: 'Video', icon: <Video size={18} /> },
  { id: 'books', label: 'Sách', icon: <Book size={18} /> },
];

export default function SearchPage() {
  const [query, setQuery] = useState('');
  const [searchType, setSearchType] = useState('text');
  const [maxResults, setMaxResults] = useState(10);
  const [results, setResults] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);
  const [hasSearched, setHasSearched] = useState(false);
  const [error, setError] = useState<string | null>(null);
  
  // State cho Dark Mode (mặc định là true - tối)
  const [darkMode, setDarkMode] = useState(true);

  const handleSearch = async (e?: React.FormEvent) => {
    if (e) e.preventDefault();
    if (!query.trim()) return;

    setLoading(true);
    setHasSearched(true);
    setError(null);
    setResults([]);

    try {
      // Gọi API Backend Python
      const params = new URLSearchParams({
        q: query,
        type: searchType,
        max_results: maxResults.toString()
      });

      const res = await fetch(`http://127.0.0.1:5000/api/search?${params.toString()}`);
      
      if (!res.ok) throw new Error('Lỗi kết nối Server Python');
      
      const data = await res.json();
      setResults(data);
    } catch (err: any) {
      console.error(err);
      setError("Không thể kết nối đến Server. Hãy đảm bảo file server.py đang chạy.");
    } finally {
      setLoading(false);
    }
  };

  // Tự động tìm lại khi đổi tab
  useEffect(() => {
    if (hasSearched && query) handleSearch();
  }, [searchType, maxResults]);

  // --- RENDERERS CHO TỪNG LOẠI KẾT QUẢ ---

  const renderTextResult = (item: any, index: number) => (
    <div key={index} className="mb-6 max-w-3xl animate-in fade-in slide-in-from-bottom-2 duration-500">
      <div className="flex items-center gap-2 text-sm text-slate-500 mb-1">
        {item.icon && <img src={item.icon} alt="" className="w-4 h-4 rounded-full" />}
        <span className="truncate">{item.href || item.url}</span>
      </div>
      <a href={item.href || item.url} target="_blank" rel="noreferrer" className="group">
        <h3 className="text-xl text-blue-500 dark:text-blue-400 group-hover:underline font-medium mb-1">
          {item.title}
        </h3>
      </a>
      <p className={`text-sm leading-relaxed ${darkMode ? 'text-slate-300' : 'text-slate-700'}`}>
        {item.body || item.snippet || item.description}
      </p>
    </div>
  );

  const renderNewsResult = (item: any, index: number) => (
    <div key={index} className={`mb-6 p-4 rounded-lg border transition-colors max-w-3xl ${darkMode ? 'bg-slate-800/30 border-slate-700 hover:bg-slate-800/50' : 'bg-white border-slate-200 hover:bg-slate-50 shadow-sm'}`}>
      <div className="flex items-center gap-2 mb-2">
        <span className="text-xs font-bold text-slate-500 uppercase tracking-wide">{item.source}</span>
        {item.date && (
          <>
            <span className="text-slate-400">•</span>
            <span className="text-xs text-slate-500 flex items-center gap-1">
              <Calendar size={12} /> {item.date}
            </span>
          </>
        )}
      </div>
      <a href={item.url} target="_blank" rel="noreferrer" className="group block">
        <h3 className="text-lg text-blue-500 dark:text-blue-400 group-hover:underline font-medium mb-2">{item.title}</h3>
      </a>
      <p className={`text-sm ${darkMode ? 'text-slate-300' : 'text-slate-700'}`}>{item.body || item.snippet}</p>
    </div>
  );

  const renderImageResult = (item: any, index: number) => (
    <div key={index} className={`group relative break-inside-avoid mb-4 rounded-lg overflow-hidden border ${darkMode ? 'border-slate-700 bg-slate-800' : 'border-slate-200 bg-gray-100'}`}>
      <a href={item.image} target="_blank" rel="noreferrer">
        <img 
          src={item.thumbnail || item.image} 
          alt={item.title} 
          className="w-full h-auto object-cover hover:opacity-90 transition-opacity"
          onError={(e) => (e.currentTarget.src = 'https://via.placeholder.com/300?text=No+Image')}
        />
      </a>
      <div className="p-3">
        <a href={item.url} target="_blank" rel="noreferrer" className="text-xs text-slate-500 hover:underline truncate block mb-1">
          {item.title}
        </a>
        <span className="text-[10px] text-slate-400 uppercase">{item.source}</span>
      </div>
    </div>
  );

  const renderVideoResult = (item: any, index: number) => (
    <div key={index} className={`flex gap-4 mb-6 p-3 rounded-xl transition-colors max-w-3xl border border-transparent ${darkMode ? 'hover:bg-slate-800/50 hover:border-slate-700' : 'hover:bg-slate-50 hover:border-slate-200'}`}>
      <div className="relative flex-shrink-0 w-40 sm:w-56 aspect-video bg-black rounded-lg overflow-hidden">
        <img 
          src={item.images?.large || item.images?.medium || item.images?.small || item.image || `https://via.placeholder.com/320x180?text=Video`} 
          alt="" 
          className="w-full h-full object-cover opacity-80"
        />
        <div className="absolute inset-0 flex items-center justify-center">
          <PlayCircle className="text-white/80 w-10 h-10 drop-shadow-lg" />
        </div>
        {item.duration && (
          <span className="absolute bottom-1 right-1 bg-black/80 text-white text-[10px] px-1.5 py-0.5 rounded">
            {item.duration}
          </span>
        )}
      </div>
      <div className="flex-1 min-w-0">
        <a href={item.content || item.url} target="_blank" rel="noreferrer" className="group">
          <h3 className="text-lg text-blue-500 dark:text-blue-400 group-hover:underline font-medium line-clamp-2 mb-1">
            {item.title}
          </h3>
        </a>
        <div className="text-xs text-slate-500 mb-2 flex items-center gap-2">
          <span className={`font-semibold ${darkMode ? 'text-slate-300' : 'text-slate-700'}`}>{item.publisher || item.uploader}</span>
          {item.views && <span>• {item.views} views</span>}
        </div>
        <p className={`text-sm line-clamp-2 ${darkMode ? 'text-slate-400' : 'text-slate-600'}`}>{item.description || item.body}</p>
      </div>
    </div>
  );

  const renderBookResult = (item: any, index: number) => (
    <div key={index} className={`mb-4 p-4 flex gap-4 rounded-lg border max-w-2xl ${darkMode ? 'bg-slate-800/40 border-slate-700' : 'bg-white border-slate-200 shadow-sm'}`}>
      <div className={`w-12 h-16 rounded flex items-center justify-center flex-shrink-0 ${darkMode ? 'bg-slate-700 text-slate-500' : 'bg-slate-100 text-slate-400'}`}>
        <Book size={24} />
      </div>
      <div>
        <a href={item.url} target="_blank" rel="noreferrer">
          <h3 className={`text-lg font-bold transition-colors ${darkMode ? 'text-slate-200 hover:text-orange-400' : 'text-slate-800 hover:text-orange-600'}`}>{item.title}</h3>
        </a>
        <div className="flex flex-wrap gap-x-4 gap-y-1 mt-1 text-sm text-slate-500">
          {item.author && <span className="flex items-center gap-1"><User size={12}/> {item.author}</span>}
          {item.publisher && <span>NXB: {item.publisher}</span>}
          {item.price && <span className="text-green-500 font-medium">{item.price}</span>}
        </div>
      </div>
    </div>
  );

  return (
    <div className={`min-h-screen transition-colors duration-300 font-sans ${darkMode ? 'bg-[#111] text-slate-200 selection:bg-orange-500/30' : 'bg-gray-50 text-slate-800 selection:bg-orange-200'}`}>
      {/* HEADER STICKY */}
      <header className={`sticky top-0 z-50 backdrop-blur border-b transition-colors duration-300 ${darkMode ? 'bg-[#111]/95 border-slate-800' : 'bg-white/90 border-slate-200 shadow-sm'}`}>
        <div className="container mx-auto px-4 py-4 max-w-6xl">
          <div className="flex flex-col md:flex-row gap-4 items-center">
            {/* Logo */}
            <div className="flex items-center gap-2 flex-shrink-0 cursor-pointer" onClick={() => {setHasSearched(false); setQuery('');}}>
              <img src="https://upload.wikimedia.org/wikipedia/en/9/90/The_DuckDuckGo_Duck.png" alt="Logo" className="w-10 h-10" />
              <span className={`font-bold text-xl tracking-tight hidden sm:block ${darkMode ? 'text-white' : 'text-slate-900'}`}>DuckSearch</span>
            </div>

            {/* Search Bar */}
            <form onSubmit={handleSearch} className="flex-1 w-full relative group">
              <div className="absolute left-4 top-3 text-slate-500 group-focus-within:text-orange-500 transition-colors">
                <Search size={18} />
              </div>
              <input 
                type="text" 
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Tìm kiếm..."
                className={`w-full border rounded-full py-2.5 pl-11 pr-24 focus:outline-none focus:border-orange-500 transition-all shadow-sm ${
                    darkMode 
                    ? 'bg-[#222] border-slate-700 text-slate-100 placeholder:text-slate-600 focus:bg-[#2a2a2a]' 
                    : 'bg-white border-slate-300 text-slate-900 placeholder:text-slate-400 focus:bg-white focus:ring-2 focus:ring-orange-500/20'
                }`}
              />
              <div className="absolute right-2 top-1.5 flex items-center gap-2">
                 <button type="submit" className="bg-orange-600 hover:bg-orange-500 text-white px-4 py-1.5 rounded-full text-sm font-medium transition-colors shadow-lg shadow-orange-900/20">
                    Tìm
                 </button>
              </div>
            </form>

            {/* Dark Mode Toggle */}
            <button 
                onClick={() => setDarkMode(!darkMode)}
                className={`p-2.5 rounded-full transition-all ${
                    darkMode 
                    ? 'bg-slate-800 text-yellow-400 hover:bg-slate-700' 
                    : 'bg-gray-100 text-slate-600 hover:bg-gray-200 hover:text-orange-500'
                }`}
                title={darkMode ? "Chuyển sang chế độ sáng" : "Chuyển sang chế độ tối"}
            >
                {darkMode ? <Sun size={20} /> : <Moon size={20} />}
            </button>
          </div>

          {/* Navigation Tabs */}
          <div className="flex items-center gap-1 mt-4 overflow-x-auto pb-1 no-scrollbar md:pl-12">
            {TABS.map((tab) => (
              <button
                key={tab.id}
                onClick={() => setSearchType(tab.id)}
                className={`flex items-center gap-2 px-4 py-2 text-sm font-medium rounded-md transition-all whitespace-nowrap border-b-2 ${
                  searchType === tab.id 
                    ? 'border-orange-500 text-orange-500 bg-orange-500/5' 
                    : `border-transparent ${darkMode ? 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/30' : 'text-slate-500 hover:text-slate-800 hover:bg-slate-100'}`
                }`}
              >
                {tab.icon}
                {tab.label}
              </button>
            ))}
            
            <div className={`ml-auto flex items-center gap-2 pl-4 border-l ${darkMode ? 'border-slate-800' : 'border-slate-200'}`}>
               <span className="text-xs text-slate-500 font-mono">Max:</span>
               <select 
                  value={maxResults} 
                  onChange={(e) => setMaxResults(Number(e.target.value))}
                  className={`border text-xs rounded px-2 py-1 focus:outline-none focus:border-orange-500 ${
                      darkMode 
                      ? 'bg-[#222] border-slate-700 text-slate-300' 
                      : 'bg-white border-slate-300 text-slate-700'
                  }`}
               >
                  <option value="5">5</option>
                  <option value="10">10</option>
                  <option value="20">20</option>
                  <option value="50">50</option>
               </select>
            </div>
          </div>
        </div>
      </header>

      {/* MAIN CONTENT */}
      <main className="container mx-auto px-4 py-6 max-w-6xl">
        {/* Initial State */}
        {!hasSearched && !loading && (
          <div className="flex flex-col items-center justify-center py-20 opacity-50">
            <LayoutGrid size={64} className={`mb-4 ${darkMode ? 'text-slate-600' : 'text-slate-300'}`} />
            <p className={`text-lg ${darkMode ? 'text-slate-500' : 'text-slate-400'}`}>Nhập từ khóa để bắt đầu tìm kiếm</p>
          </div>
        )}

        {/* Loading */}
        {loading && (
          <div className="py-10 max-w-3xl animate-pulse space-y-6">
             {[1,2,3].map(i => (
                <div key={i}>
                   <div className={`h-4 w-1/3 rounded mb-2 ${darkMode ? 'bg-slate-800' : 'bg-slate-200'}`}></div>
                   <div className={`h-6 w-2/3 rounded mb-2 ${darkMode ? 'bg-slate-800' : 'bg-slate-200'}`}></div>
                   <div className={`h-16 w-full rounded ${darkMode ? 'bg-slate-800' : 'bg-slate-200'}`}></div>
                </div>
             ))}
          </div>
        )}

        {/* Error */}
        {error && (
          <div className="p-4 bg-red-900/20 border border-red-900/50 text-red-400 rounded-lg text-center my-8">
            {error}
          </div>
        )}

        {/* Results */}
        {!loading && !error && hasSearched && (
          <>
            <div className="text-xs text-slate-500 mb-4 font-mono">
              Đã tìm thấy {results.length} kết quả
            </div>
            
            {results.length === 0 ? (
               <div className="text-center py-10 text-slate-500">
                  <p>Không tìm thấy kết quả nào phù hợp.</p>
               </div>
            ) : (
              <div className={searchType === 'images' ? 'columns-2 md:columns-3 lg:columns-4 gap-4 space-y-4' : ''}>
                {results.map((item, index) => {
                  if (searchType === 'images') return renderImageResult(item, index);
                  if (searchType === 'videos') return renderVideoResult(item, index);
                  if (searchType === 'news') return renderNewsResult(item, index);
                  if (searchType === 'books') return renderBookResult(item, index);
                  return renderTextResult(item, index);
                })}
              </div>
            )}
          </>
        )}
      </main>
    </div>
  );
}