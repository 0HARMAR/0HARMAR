package com.example.demo.service;

import org.springframework.web.multipart.MultipartFile;

public interface FileUploadService {
    void saveFile(MultipartFile file);

    void setEncoding(String encoding);
}
