package com.example.demo.model.entity;

import jakarta.persistence.Entity; // Spring Boot 3.x 使用 jakarta
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;

@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name; // 确保字段名与数据库列名一致
    private String email;

    // 必须有无参构造函数
    public User() {}

    // 必须有 Getter 方法（否则 JSON 序列化失败）
    public Long getId() { return id; }
    public String getName() { return name; }
    public String getEmail() { return email; }

    // Setter 方法（插入数据时需要）
    public void setId(Long id) { this.id = id; }
    public void setName(String name) { this.name = name; }
    public void setEmail(String email) { this.email = email; }
}