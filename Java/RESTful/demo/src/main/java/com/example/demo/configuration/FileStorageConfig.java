package com.example.demo.configuration;

import lombok.Data;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Configuration;
import org.springframework.stereotype.Component;
import org.springframework.validation.annotation.Validated;

@ConfigurationProperties(prefix = "file")
@Validated
@Data
@Component
public class FileStorageConfig {

    private String uploadDir = "/data/upload";
    private String outputDir = "/data/output";
    private String compileFileId;
}