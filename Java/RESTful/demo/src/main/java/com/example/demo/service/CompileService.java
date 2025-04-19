package com.example.demo.service;

import com.example.demo.model.entity.CompileConfig;
import org.springframework.web.multipart.MultipartFile;

public interface CompileService {
    MultipartFile startCompile(CompileConfig option);
}
