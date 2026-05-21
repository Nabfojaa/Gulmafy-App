"""
Reverse Image Search Utility - Search for weed images using Google Images
"""
import requests
import base64
from PIL import Image
import io
import streamlit as st
from urllib.parse import quote

def get_google_images_search_url(image_path: str) -> str:
    """
    Generate Google Images reverse search URL from local image
    
    Args:
        image_path: Path to local image file
        
    Returns:
        URL for Google Images search
    """
    # Read and encode image as base64
    with open(image_path, 'rb') as f:
        img_data = f.read()
    
    # Google Images reverse search URL (simplified approach)
    # Using Google Lens which is the modern reverse image search
    return f"https://lens.google.com/uploadbyurl?url=file://{image_path}"


def display_google_search_results(image_bytes) -> str:
    """
    Display Google Images search results embedded in the page
    
    Args:
        image_bytes: Image data in bytes
        
    Returns:
        HTML for embedded search results
    """
    try:
        # Convert image to base64
        img_b64 = base64.b64encode(image_bytes).decode()
        
        # Create data URL
        data_url = f"data:image/png;base64,{img_b64}"
        
        # Google Images reverse search - embedded approach
        # This uses Google's reverse image search interface
        search_url = f"https://www.google.com/searchbyimage?image_url={quote(data_url)}"
        
        return search_url
    except Exception as e:
        return None


def display_alternative_search_results(image_bytes) -> dict:
    """
    Provide multiple search options for the image
    
    Args:
        image_bytes: Image data in bytes
        
    Returns:
        Dictionary with different search options
    """
    try:
        img_b64 = base64.b64encode(image_bytes).decode()
        data_url = f"data:image/png;base64,{img_b64}"
        
        search_options = {
            "google_images": f"https://www.google.com/searchbyimage?image_url={quote(data_url)}",
            "google_lens": "https://lens.google.com",
            "bing_images": "https://www.bing.com/images/search?view=detailv2&iss=sbiupload",
        }
        
        return search_options
    except Exception as e:
        return {}


def create_search_results_html(image_bytes, search_url: str) -> str:
    """
    Create HTML display for search results with embedded iframe
    
    Args:
        image_bytes: Original image bytes
        search_url: URL to search results
        
    Returns:
        HTML string for display
    """
    img_b64 = base64.b64encode(image_bytes).decode()
    
    html = f"""
    <div style="background: linear-gradient(135deg, rgba(59, 130, 246, 0.08) 0%, rgba(147, 197, 253, 0.08) 100%);
                border: 2px solid rgba(59, 130, 246, 0.3);
                border-radius: 20px;
                padding: 28px;
                margin: 20px 0;">
        <p style="color: #1B4332; font-weight: 700; font-size: 1.2rem; margin: 0 0 16px 0;">🔍 Hasil Pencarian Visual (Reverse Image Search)</p>
        
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">
            <!-- Original Image -->
            <div>
                <p style="color: #666; font-weight: 700; margin: 0 0 10px 0; font-size: 0.9rem;">Foto Asli yang Dicari:</p>
                <img src="data:image/png;base64,{img_b64}" 
                     style="width: 100%; border-radius: 16px; box-shadow: 0 8px 24px rgba(27, 67, 50, 0.12);" />
            </div>
            
            <!-- Search Results Info -->
            <div style="display: flex; flex-direction: column; justify-content: center;">
                <div style="background: white; border-radius: 16px; padding: 20px; border: 1px solid rgba(59, 130, 246, 0.2);">
                    <p style="margin: 0 0 12px 0; color: #1B4332; font-weight: 700; font-size: 1rem;">📊 Hasil Pencarian:</p>
                    <p style="margin: 0 0 16px 0; color: #2D6A4F; font-size: 0.95rem; line-height: 1.6;">
                        Sistem melakukan pencarian visual terbalik ke Google Images untuk menemukan gulma serupa, referensi visual, dan informasi terkait.
                    </p>
                    <a href="{search_url}" target="_blank" style="display: inline-block; padding: 12px 28px; background: linear-gradient(135deg, #3B82F6 0%, #2563EB 100%); color: white; border-radius: 10px; text-decoration: none; font-weight: 700; cursor: pointer; transition: all 0.3s ease;"
                       onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 8px 24px rgba(59, 130, 246, 0.3)';"
                       onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none';">
                        ✨ Lihat Hasil Pencarian di Google Images
                    </a>
                </div>
            </div>
        </div>
        
        <div style="background: rgba(255, 255, 255, 0.6); border-radius: 12px; padding: 16px; margin-top: 16px;">
            <p style="color: #666; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                💡 <strong>Tips Penggunaan:</strong> Klik tombol di atas untuk melihat hasil pencarian dari Google Images. 
                Hasil akan menunjukkan gulma serupa, referensi visual, dan informasi terkait yang dapat membantu identifikasi.
            </p>
        </div>
    </div>
    """
    
    return html


def create_advanced_search_panel() -> str:
    """
    Create HTML for advanced search options
    
    Returns:
        HTML string with search options
    """
    html = """
    <div style="background: linear-gradient(135deg, rgba(168, 85, 247, 0.08) 0%, rgba(217, 119, 249, 0.08) 100%);
                border: 2px solid rgba(168, 85, 247, 0.3);
                border-radius: 20px;
                padding: 28px;
                margin: 20px 0;">
        <p style="color: #1B4332; font-weight: 700; font-size: 1.1rem; margin: 0 0 16px 0;">🎯 Opsi Pencarian Lanjutan</p>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px;">
            <a href="https://lens.google.com" target="_blank" style="padding: 16px; background: white; border: 2px solid #9333EA; border-radius: 12px; text-align: center; text-decoration: none; transition: all 0.3s ease; cursor: pointer;"
               onmouseover="this.style.background='#f5f3ff'; this.style.transform='translateY(-2px)';"
               onmouseout="this.style.background='white'; this.style.transform='translateY(0)';">
                <div style="font-size: 1.5rem; margin-bottom: 8px;">🔎</div>
                <p style="margin: 0; color: #1B4332; font-weight: 700; font-size: 0.9rem;">Google Lens</p>
                <p style="margin: 4px 0 0 0; color: #666; font-size: 0.8rem;">Analisis visual modern</p>
            </a>
            
            <a href="https://www.google.com/images" target="_blank" style="padding: 16px; background: white; border: 2px solid #3B82F6; border-radius: 12px; text-align: center; text-decoration: none; transition: all 0.3s ease; cursor: pointer;"
               onmouseover="this.style.background='#eff6ff'; this.style.transform='translateY(-2px)';"
               onmouseout="this.style.background='white'; this.style.transform='translateY(0)';">
                <div style="font-size: 1.5rem; margin-bottom: 8px;">🖼️</div>
                <p style="margin: 0; color: #1B4332; font-weight: 700; font-size: 0.9rem;">Google Images</p>
                <p style="margin: 4px 0 0 0; color: #666; font-size: 0.8rem;">Cari gambar serupa</p>
            </a>
            
            <a href="https://www.bing.com/images" target="_blank" style="padding: 16px; background: white; border: 2px solid #16A34A; border-radius: 12px; text-align: center; text-decoration: none; transition: all 0.3s ease; cursor: pointer;"
               onmouseover="this.style.background='#f0fdf4'; this.style.transform='translateY(-2px)';"
               onmouseout="this.style.background='white'; this.style.transform='translateY(0)';">
                <div style="font-size: 1.5rem; margin-bottom: 8px;">🌍</div>
                <p style="margin: 0; color: #1B4332; font-weight: 700; font-size: 0.9rem;">Bing Images</p>
                <p style="margin: 4px 0 0 0; color: #666; font-size: 0.8rem;">Search alternatif</p>
            </a>
        </div>
    </div>
    """
    
    return html
