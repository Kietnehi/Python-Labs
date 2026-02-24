<div align="center">

<p>
  <img src="https://raw.githubusercontent.com/HKUDS/RAG-Anything/main/assets/logo.png"
       width="120"
       height="120"
       alt="RAG-Anything Logo" />
</p>

# 🚀 RAG-Anything: All-in-One RAG Framework

<p>
  <a href="https://trendshift.io/repositories/14959" target="_blank">
    <img src="https://trendshift.io/api/badge/repositories/14959"
         alt="HKUDS/RAG-Anything | Trendshift"
         width="250"
         height="55"/>
  </a>
</p>

<p>
  <img src="https://readme-typing-svg.herokuapp.com?font=Orbitron&size=24&duration=3000&pause=1000&color=00D9FF&center=true&vCenter=true&width=600&lines=Welcome+to+RAG-Anything;Next-Gen+Multimodal+RAG+System;Powered+by+Advanced+AI+Technology"
       alt="Typing Animation" />
</p>

<p>
  <a href="https://github.com/HKUDS/RAG-Anything">
    <img src="https://img.shields.io/badge/🔥Project-Page-00d9ff?style=for-the-badge&logo=github&logoColor=white"/>
  </a>
  <a href="https://arxiv.org/abs/2510.12323">
    <img src="https://img.shields.io/badge/📄arXiv-2510.12323-ff6b6b?style=for-the-badge&logo=arxiv&logoColor=white"/>
  </a>
  <a href="https://github.com/HKUDS/LightRAG">
    <img src="https://img.shields.io/badge/⚡Based%20on-LightRAG-4ecdc4?style=for-the-badge"/>
  </a>
</p>

<p>
  <a href="https://github.com/HKUDS/RAG-Anything/stargazers">
    <img src="https://img.shields.io/github/stars/HKUDS/RAG-Anything?style=for-the-badge&logo=star&logoColor=white"/>
  </a>
  <img src="https://img.shields.io/badge/🐍Python-3.10-4ecdc4?style=for-the-badge&logo=python&logoColor=white"/>
  <a href="https://pypi.org/project/raganything/">
    <img src="https://img.shields.io/pypi/v/raganything.svg?style=for-the-badge&logo=pypi&logoColor=white"/>
  </a>
  <a href="https://github.com/astral-sh/uv">
    <img src="https://img.shields.io/badge/⚡uv-Ready-ff6b6b?style=for-the-badge"/>
  </a>
</p>

<p>
  <a href="https://discord.gg/yF2MmDJyGJ">
    <img src="https://img.shields.io/badge/💬Discord-Community-7289da?style=for-the-badge&logo=discord&logoColor=white"/>
  </a>
  <a href="https://github.com/HKUDS/RAG-Anything/issues/7">
    <img src="https://img.shields.io/badge/💬WeChat-Group-07c160?style=for-the-badge"/>
  </a>
</p>

<p>
  <a href="README_zh.md">
    <img src="https://img.shields.io/badge/🇨🇳中文版-black?style=for-the-badge"/>
  </a>
  <a href="README.md">
    <img src="https://img.shields.io/badge/🇺🇸English-black?style=for-the-badge"/>
  </a>
</p>

</div>

---

<div align="center">
  <a href="#-quick-start">
    <img src="https://img.shields.io/badge/Quick%20Start-Get%20Started%20Now-00d9ff?style=for-the-badge&logo=rocket&logoColor=white"/>
  </a>
</div>

---

<div align="center">
  <a href="https://litewrite.ai">
    <img src="https://raw.githubusercontent.com/HKUDS/RAG-Anything/main/assets/LiteWrite.png"
         width="56"
         height="56"
         alt="LiteWrite"/>
  </a>
  <br/><br/>
  <a href="https://litewrite.ai">
    <img src="https://img.shields.io/badge/🚀%20LiteWrite-AI%20Native%20LaTeX%20Editor-ff6b6b?style=for-the-badge"/>
  </a>
</div>




---

<div align="center">
  <img src="https://raw.githubusercontent.com/HKUDS/RAG-Anything/main/assets/rag_anything_framework.png"
       alt="RAG-Anything Framework Architecture"
       width="100%"/>
</div>
---

# 🚀 RAG-Anything: Framework RAG Tất Cả Trong Một

> Hệ thống RAG đa phương thức (Multimodal RAG) xử lý văn bản, hình ảnh, bảng biểu, công thức toán và nhiều định dạng tài liệu khác trong một pipeline thống nhất.

---

## 🎯 Giới Thiệu

**RAG-Anything** là một framework RAG đa phương thức được xây dựng trên nền tảng LightRAG, cho phép:

- Xử lý tài liệu chứa nhiều loại nội dung (text, image, table, equation…)
- Truy vấn thông minh dựa trên Vector Search kết hợp Knowledge Graph
- Hỗ trợ nhiều định dạng: PDF, Office, ảnh, Markdown, TXT
- Tích hợp Vision-Language Model (VLM) để phân tích hình ảnh trong ngữ cảnh

Khác với hệ thống RAG truyền thống chỉ xử lý văn bản, RAG-Anything cung cấp khả năng truy xuất và hiểu nội dung đa phương thức trong một hệ thống thống nhất.

---

## ✨ Tính Năng Chính

- 🔄 Pipeline xử lý đa phương thức đầu-cuối  
- 📄 Hỗ trợ nhiều định dạng tài liệu  
- 🧠 Phân tích chuyên biệt cho ảnh, bảng và công thức toán  
- 🔗 Xây dựng Multimodal Knowledge Graph  
- ⚡ Truy xuất Hybrid (Vector + Graph)  
- 🎯 Truy vấn nâng cao với VLM  
- 📋 Chèn trực tiếp danh sách nội dung đã parse  

---

## 🏗️ Kiến Trúc Hệ Thống

Pipeline xử lý gồm 5 giai đoạn chính:

1. 📄 Document Parsing  
2. 🧠 Multimodal Content Processing  
3. 🔍 Knowledge Graph Construction  
4. ⚖️ Weighted Relationship Scoring  
5. 🚀 Hybrid Retrieval (Vector + Graph)  

```mermaid
graph TD
  %% Giai đoạn 1: Universal Indexing
  subgraph Phase1 [1. Chỉ mục hóa vạn năng - Universal Indexing]
    Input[Tài liệu đa phương thức: PDF, Doc, Ảnh...] --> Decomp[Phân rã thành các đơn vị kiến thức nguyên tử]
    Decomp --> Units{Loại dữ liệu}
    Units -->|Văn bản| Txt[Đoạn văn bản]
    Units -->|Hình ảnh| Img[Ảnh + Chú thích]
    Units -->|Bảng biểu| Tab[Cấu trúc hàng/cột]
    Units -->|Công thức| Equ[Biểu thức toán học]
  end

  %% Giai đoạn 2: Dual-Graph Construction
  subgraph Phase2 [2. Xây dựng Đồ thị kép - Dual-Graph Construction]
    Txt --> TKG[Đồ thị tri thức dựa trên văn bản]
    Img & Tab & Equ --> CMKG[Đồ thị tri thức xuyên phương thức - Cross-Modal KG]
    TKG & CMKG --> Fusion[Hợp nhất thực thể & Tạo không gian nhúng chung]
  end

  %% Giai đoạn 3: Hybrid Retrieval
  subgraph Phase3 [3. Truy xuất hỗn hợp - Hybrid Retrieval]
    Query[Câu hỏi người dùng] --> Analysis[Phân tích phương thức truy vấn]
    Analysis --> Semantic[Tìm kiếm tương đồng ngữ nghĩa - Vector]
    Analysis --> Structural[Duyệt đồ thị theo cấu trúc - Multi-hop]
    Semantic & Structural --> Unified[Hợp nhất kết quả ứng viên]
  end

  %% Giai đoạn 4: Synthesis
  subgraph Phase4 [4. Tổng hợp phản hồi - Synthesis]
    Unified --> Context[Xây dựng ngữ cảnh văn bản]
    Unified --> Visual[Phục hồi nội dung hình ảnh gốc - Dereferencing]
    Context & Visual --> VLM[Mô hình Vision-Language - VLM]
    VLM --> Response[Câu trả lời chính xác & Đầy đủ ngữ cảnh]
  end

  %% Định nghĩa màu sắc
  style Phase1 fill:#f9f,stroke:#333,stroke-width:2px
  style Phase2 fill:#bbf,stroke:#333,stroke-width:2px
  style Phase3 fill:#bfb,stroke:#333,stroke-width:2px
  style Phase4 fill:#fdb,stroke:#333,stroke-width:2px
```

---

## 📦 Cài Đặt

### 🔹 Cài từ PyPI (Khuyến nghị)

```bash
pip install raganything
```

Cài đầy đủ tính năng:

```bash
pip install "raganything[all]"
```

Cài theo từng module:

```bash
pip install "raganything[image]"
pip install "raganything[text]"
```

---

## ⚠️ Yêu Cầu Xử Lý Office

Để xử lý file `.doc`, `.ppt`, `.xls` cần cài LibreOffice:

**macOS:**
```bash
brew install --cask libreoffice
```

**Ubuntu:**
```bash
sudo apt install libreoffice
```

---

## 🧠 Ví Dụ Sử Dụng Cơ Bản

### 1️⃣ Xử lý tài liệu hoàn chỉnh

```python
import asyncio
from raganything import RAGAnything, RAGAnythingConfig

async def main():
    config = RAGAnythingConfig(
        working_dir="./rag_storage",
        parser="mineru",
        parse_method="auto",
        enable_image_processing=True,
        enable_table_processing=True,
        enable_equation_processing=True,
    )

    rag = RAGAnything(config=config)

    await rag.process_document_complete(
        file_path="document.pdf",
        output_dir="./output"
    )

    result = await rag.aquery(
        "Tóm tắt nội dung chính của tài liệu",
        mode="hybrid"
    )

    print(result)

asyncio.run(main())
```

---

### 2️⃣ Truy vấn đa phương thức

```python
result = await rag.aquery_with_multimodal(
    "Giải thích công thức sau",
    multimodal_content=[{
        "type": "equation",
        "latex": "P(d|q) = \\frac{P(q|d)P(d)}{P(q)}",
        "equation_caption": "Xác suất liên quan tài liệu"
    }],
    mode="hybrid"
)
```

---

### 3️⃣ Batch Processing

```python
await rag.process_folder_complete(
    folder_path="./documents",
    output_dir="./output",
    recursive=True
)
```

---

## 📋 Định Dạng Content List

```python
content_list = [
    {"type": "text", "text": "Nội dung văn bản", "page_idx": 0},
    {"type": "image", "img_path": "/abs/path/image.jpg", "page_idx": 1},
    {"type": "table", "table_body": "|A|B|", "page_idx": 2},
    {"type": "equation", "latex": "E=mc^2", "page_idx": 3}
]
```

Chèn trực tiếp:

```python
await rag.insert_content_list(
    content_list=content_list,
    file_path="paper.pdf"
)
```

---

## 🔧 Cấu Hình Environment

Tạo file `.env`:

```
OPENAI_API_KEY=your_key
OPENAI_BASE_URL=your_base_url
OUTPUT_DIR=./output
PARSER=mineru
PARSE_METHOD=auto
```

---

## 🧪 Các Loại Nội Dung Hỗ Trợ

### 📄 Định dạng tài liệu
- PDF  
- DOC / DOCX  
- PPT / PPTX  
- XLS / XLSX  
- JPG / PNG / BMP / TIFF / GIF / WebP  
- TXT / MD  

### 🧩 Thành phần đa phương thức
- Văn bản  
- Hình ảnh  
- Bảng dữ liệu  
- Công thức LaTeX  
- Nội dung tùy chỉnh  

---

## 📖 Trích Dẫn Học Thuật

```bibtex
@misc{guo2025raganythingallinoneragframework,
  title={RAG-Anything: All-in-One RAG Framework},
  author={Zirui Guo and Xubin Ren and Lingrui Xu and Jiahao Zhang and Chao Huang},
  year={2025},
  eprint={2510.12323},
  archivePrefix={arXiv},
  primaryClass={cs.AI}
}
```

---

# ⭐ Cảm ơn bạn đã sử dụng RAG-Anything!