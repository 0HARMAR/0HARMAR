package com.example.demo;

import org.junit.jupiter.api.Test;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import com.example.demo.dao.mapper.CompileTaskMapper;



@SpringBootTest(classes = DemoApplication.class)
@MapperScan("com.example.demo.dao.mapper") 
class DemoApplicationTests {

	@Test
	void contextLoads() {
	}

	@Test
	public void helloTest(){
		System.out.println("hello");
	}

	@Autowired
	private CompileTaskMapper compileTaskMapper;
	@Test
	public void compileTaskMapperTest(){
		System.out.println(compileTaskMapper.findAll());;
	}
}
