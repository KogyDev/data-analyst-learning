import { useState } from 'react';
import { Linkedin, Github, Mail, X } from 'lucide-react';

const Gallery = () => {
  const [expandedId, setExpandedId] = useState(null);

  const socialLinks = [
    {
      icon: Linkedin,
      url: "https://www.linkedin.com/in/matheus-cornedi-614224213/",
      label: "LinkedIn"
    },
    {
      icon: Github,
      url: "https://github.com/KogyDev",
      label: "GitHub"
    },
    {
      icon: Mail,
      url: "mailto:matheus.r.cornedi@gmail.com",
      label: "Email"
    }
  ];

  const galleryItems = [
    {
      id: 1,
      title: "Slide",
      description: "Texto sobre modelo de slides",
      color: "bg-emerald-600",
      mediaUrl: "C:\Users\Gamer\Pictures\Screenshots\slide.png",
      mediaType: "image"
    },
    {
      id: 2,
      title: "Infográfico",
      description: "Texto sobre modelo de infográficos",
      color: "bg-blue-600",
      mediaUrl: "C:\Users\Gamer\Pictures\Screenshots\infogra.png",
      mediaType: "image"
    },
    {
      id: 3,
      title: "Mapa Mental",
      description: "Texto sobre modelo de Mapa Mental",
      color: "bg-purple-600",
      mediaUrl: "/api/placeholder/800/600",
      mediaType: "gif"
    },
    {
      id: 4,
      title: "One Pager",
      description: "Texto sobre modelo de One Pager",
      color: "bg-red-600",
      mediaUrl: "/api/placeholder/800/600",
      mediaType: "image"
    },
    {
      id: 5,
      title: "Dashboard",
      description: "Texto sobre modelo de Dashboard",
      color: "bg-yellow-600",
      mediaUrl: "/api/placeholder/800/600",
      mediaType: "video"
    },
     
    
  ];

  const renderMedia = (item) => {
    switch (item.mediaType) {
      case 'video':
        return (
          <video 
            className="w-full rounded-lg shadow-lg transform transition-transform duration-700 hover:scale-105" 
            controls
            autoPlay
            muted
          >
            <source src={item.mediaUrl} type="video/mp4" />
            Seu navegador não suporta vídeos.
          </video>
        );
      case 'gif':
        return (
          <img 
            src={item.mediaUrl} 
            alt={item.title}
            className="w-full rounded-lg shadow-lg transform transition-transform duration-700 hover:scale-105"
          />
        );
      default:
        return (
          <img 
            src={item.mediaUrl} 
            alt={item.title}
            className="w-full rounded-lg shadow-lg transform transition-transform duration-700 hover:scale-105"
          />
        );
    }
  };

  const Card = ({ item }) => {
    const isExpanded = expandedId === item.id;
    
    return (
      <div
        className={`
          relative
          overflow-hidden
          rounded-lg 
          transition-all 
          duration-700
          ease-in-out
          cursor-pointer
          ${item.color}
          ${isExpanded ? 'col-span-3 row-span-2' : 'hover:shadow-xl hover:scale-105'}
          transform origin-center
        `}
        onClick={() => setExpandedId(isExpanded ? null : item.id)}
        style={{
          transition: 'all 0.7s cubic-bezier(0.4, 0, 0.2, 1)'
        }}
      >
        <div className={`
          p-6 
          h-full 
          transition-all 
          duration-700
          ease-in-out
          ${isExpanded ? 'scale-100' : 'transform'}
        `}>
          <div className="flex justify-between items-start mb-4">
            <h2 className={`
              text-2xl 
              font-bold 
              text-white
              transition-all
              duration-700
              ${isExpanded ? 'text-3xl' : ''}
            `}>{item.title}</h2>
            {isExpanded && (
              <button 
                onClick={(e) => {
                  e.stopPropagation();
                  setExpandedId(null);
                }}
                className="text-white hover:text-gray-200 transition-colors duration-300"
              >
                <X size={24} />
              </button>
            )}
          </div>
          
          <div className={`
            transition-all 
            duration-700
            ease-in-out
            ${isExpanded 
              ? 'opacity-100 max-h-screen transform translate-y-0' 
              : 'opacity-90 max-h-20 transform translate-y-0'
            }
          `}>
            {isExpanded ? (
              <div className="space-y-4 animate-fadeIn">
                <div className="transform transition-all duration-700 ease-in-out">
                  {renderMedia(item)}
                </div>
                <p className="text-white text-lg mt-4 leading-relaxed animate-slideUp">
                  {item.description}
                </p>
              </div>
            ) : (
              <p className="text-white opacity-90 line-clamp-2">
                {item.description}
              </p>
            )}
          </div>
        </div>
      </div>
    );
  };

  return (
    <div className="min-h-screen bg-gray-100 p-4 relative">
      {/* Social Icons */}
      <div className="absolute top-4 right-4 flex gap-3 z-10">
        {socialLinks.map((social, index) => (
          <a
            key={index}
            href={social.url}
            target="_blank"
            rel="noopener noreferrer"
            className="p-2 bg-white rounded-full shadow-md hover:shadow-lg transform hover:scale-110 transition-all duration-300"
            aria-label={social.label}
          >
            <social.icon size={20} className="text-gray-600 hover:text-gray-800" />
          </a>
        ))}
      </div>

      {/* Header */}
      <header className="text-center mb-8 pt-16">
        <h1 className="text-4xl font-bold text-gray-800 mb-2">Matheus Cornedi</h1>
        <p className="text-gray-600">Algumas amostras de materiais já criados editados por mim</p>
      </header>

      {/* Grid de Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 max-w-6xl mx-auto">
        {galleryItems.map((item) => (
          <Card key={item.id} item={item} />
        ))}
      </div>

      <style jsx global>{`
        @keyframes fadeIn {
          from { opacity: 0; }
          to { opacity: 1; }
        }
        
        @keyframes slideUp {
          from {
            opacity: 0;
            transform: translateY(20px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
        
        .animate-fadeIn {
          animation: fadeIn 0.7s ease-in-out;
        }
        
        .animate-slideUp {
          animation: slideUp 0.7s ease-out;
        }
      `}</style>
    </div>
  );
};

export default Gallery;
