from coffeehr.pipeline.interface import Pipeline

pipeline = Pipeline(
    name="Employees",
    get_options=("POST", "SYN_EL_NHANVIEN"),
    transform=lambda rows: [
        {
            "DienThoai": row.get("DienThoai"),
            "Email": row.get("Email"),
            "Ho": row.get("Ho"),
            "HoTen": row.get("HoTen"),
            "LastUpdate": row.get("LastUpdate"),
            "LoaiTaiKhoan": row.get("LoaiTaiKhoan"),
            "MaChucDanh": row.get("MaChucDanh"),
            "MaChucVu": row.get("MaChucVu"),
            "MaNhanVien": row.get("MaNhanVien"),
            "MaNhanVienQuanLy": row.get("MaNhanVienQuanLy"),
            "MaPhongBan": row.get("MaPhongBan"),
            "MatKhau": row.get("MatKhau"),
            "NgayBatDauLam": row.get("NgayBatDauLam"),
            "NgayNghiViec": row.get("NgayNghiViec"),
            "TenChucDanh": row.get("TenChucDanh"),
            "TenChucVu": row.get("TenChucVu"),
            "TenDangNhap": row.get("TenDangNhap"),
            "TrangThai": row.get("TrangThai"),
            "ViTriGioCong": row.get("ViTriGioCong"),
        }
        for row in rows
    ],
    schema=[
        {"name": "DienThoai", "type": "STRING"},
        {"name": "Email", "type": "STRING"},
        {"name": "Ho", "type": "STRING"},
        {"name": "HoTen", "type": "STRING"},
        {"name": "LastUpdate", "type": "TIMESTAMP"},
        {"name": "LoaiTaiKhoan", "type": "BOOLEAN"},
        {"name": "MaChucDanh", "type": "NUMERIC"},
        {"name": "MaChucVu", "type": "NUMERIC"},
        {"name": "MaNhanVien", "type": "STRING"},
        {"name": "MaNhanVienQuanLy", "type": "STRING"},
        {"name": "MaPhongBan", "type": "NUMERIC"},
        {"name": "MatKhau", "type": "STRING"},
        {"name": "NgayBatDauLam", "type": "TIMESTAMP"},
        {"name": "NgayNghiViec", "type": "TIMESTAMP"},
        {"name": "TenChucDanh", "type": "STRING"},
        {"name": "TenChucVu", "type": "STRING"},
        {"name": "TenDangNhap", "type": "STRING"},
        {"name": "TrangThai", "type": "BOOLEAN"},
        {"name": "ViTriGioCong", "type": "STRING"},
    ],
)
