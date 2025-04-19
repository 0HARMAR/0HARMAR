package com.example.demo.service;

import com.example.demo.configuration.FileStorageConfig;
import com.example.demo.dao.mapper.CompileTaskMapper;
import com.example.demo.dao.mapper.FileInfoMapper;
import com.example.demo.model.entity.CompileConfig;
import com.example.demo.model.entity.CompileTask;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.UUID;

@Service
public class CompileServiceImpl implements CompileService{
    private String compileFileId;

    @Autowired
    CompileServiceImpl(FileStorageConfig fileStorageConfig){
        this.compileFileId = fileStorageConfig.getCompileFileId();
    }

    @Autowired
    FileInfoMapper fileInfoMapper;

    @Autowired
    CompileTaskMapper compileTaskMapper;
    @Override
    public MultipartFile startCompile(CompileConfig option) {
        // 创建新编译任务
        CompileTask compileTask = new CompileTask();
        compileTask.setTaskId(UUID.randomUUID().toString());
        compileTaskMapper.addTask(compileTask);

        fileInfoMapper.updateFileTaskIdByFileId(compileFileId);
        try {
            int exitCode = startCompileProcess(findFilePathById(compileFileId),findFileNameById(compileFileId),option);
        } catch (IOException | InterruptedException e) {
            throw new RuntimeException(e);
        }

    }

    public static int startCompileProcess(String sourceFile, String outputFile,CompileConfig option) throws IOException, InterruptedException {
        Process process = new ProcessBuilder(
                option.getCompilerType(),
                option.getCompilerArgs(),
                "-o", outputFile,
                sourceFile
        ).redirectErrorStream(true).start();

        // 实时获取输出信息
        BufferedReader reader = new BufferedReader(
                new InputStreamReader(process.getInputStream()));
        String line;
        while ((line = reader.readLine()) != null) {
            System.out.println("[GCC] " + line);
        }

        return process.waitFor();
    }

    private String findFilePathById(String fileId) {
        return fileInfoMapper.findFilePathById(fileId);
    }

    private String findFileNameById(String fileId) {return fileInfoMapper.findFileNameById(fileId);}
}
