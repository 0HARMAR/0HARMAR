package com.example.demo.controller;

import com.example.demo.common.Result;
import com.example.demo.model.entity.CompileConfig;
import com.example.demo.service.CompileServiceImpl;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import com.example.demo.service.CompileService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.mvc.method.annotation.SseEmitter;


@RestController
public class CompileController {
    private SseEmitter emitter = new SseEmitter();
    @Autowired
    private CompileServiceImpl compileServiceImpl;

    @GetMapping("setSseEmitter")
    public SseEmitter setSseEmitter(@RequestParam("file") MultipartFile file) {
        emitter = new SseEmitter();
        return emitter;
    }
    @PostMapping("compile")
    public ResponseEntity<Result<MultipartFile>> handleCompile(@RequestParam("option")@RequestBody CompileConfig option) {
        compileServiceImpl.startCompile(option);
        return ;
    }
    
}
