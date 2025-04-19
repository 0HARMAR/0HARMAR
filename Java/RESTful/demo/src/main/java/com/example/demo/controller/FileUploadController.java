package com.example.demo.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import com.example.demo.service.FileUploadServiceImpl;
import lombok.extern.slf4j.Slf4j;

@RestController
@Slf4j
public class FileUploadController {
    
    @Autowired
    private FileUploadServiceImpl fileUploadServiceImpl;

    @PostMapping("/upload")
    public ResponseEntity<String> handleFileUpload(@RequestParam("file") MultipartFile file) {
            fileUploadServiceImpl.saveFile(file);
            return ResponseEntity.ok("文件上传成功: " + file.getOriginalFilename());
    }

    @PostMapping("/encoding")
    public ResponseEntity<String> handleFileEncoding(@RequestParam("encoding") String encoding) {
        fileUploadServiceImpl.setEncoding(encoding);
        return ResponseEntity.ok("编码选择成功: " + encoding);
    }
}
