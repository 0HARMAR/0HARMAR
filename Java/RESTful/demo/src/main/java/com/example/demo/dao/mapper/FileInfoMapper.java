package com.example.demo.dao.mapper;

import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;

import com.example.demo.model.entity.FileInfo;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;

@Mapper
public interface FileInfoMapper {
    @Insert({
        "INSERT INTO file_info (file_id, file_type, file_path, file_size, hash_sha256, encoding)",
        "VALUES (",
        "#{fileId}, #{fileType}, #{filePath}, #{fileSize}, #{hashSha256},",
        "#{encoding})"
    })
    public void addFile(FileInfo fileInfo);

    @Select("select file_path from file_info where file_id = #{fileId}")
    public String findFilePathById(String fileId);

    @Select("select file_name from file_info where file_id = #{fileId}")
    String findFileNameById(String fileId);

    @Update("update compile_task set task_id = #{taskId}")
    void updateFileTaskIdByFileId(String taskId);
}
