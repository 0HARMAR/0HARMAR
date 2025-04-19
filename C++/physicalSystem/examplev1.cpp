#include <iostream>
#include <vector>
#include <cmath>

// 向量类
struct Vector2 {
    float x, y;

    Vector2() : x(0), y(0) {}
    Vector2(float x, float y) : x(x), y(y) {}

    Vector2 operator+(const Vector2& other) const {
        return Vector2(x + other.x, y + other.y);
    }

    Vector2 operator-(const Vector2& other) const {
        return Vector2(x - other.x, y - other.y);
    }

    Vector2 operator*(float scalar) const {
        return Vector2(x * scalar, y * scalar);
    }

    float length() const {
        return std::sqrt(x * x + y * y);
    }

    Vector2 normalized() const {
        float len = length();
        return Vector2(x / len, y / len);
    }
};

// 物体类
class Body {
public:
    Vector2 position;
    Vector2 velocity;
    Vector2 force;
    float mass;
    float radius;

    Body(Vector2 pos, float m, float r) 
        : position(pos), mass(m), radius(r), velocity(0, 0), force(0, 0) {}

    void applyForce(const Vector2& f) {
        force = force + f;
    }

    void update(float dt) {
        Vector2 acceleration = force * (1.0f / mass);
        velocity = velocity + acceleration * dt;
        position = position + velocity * dt;
        force = Vector2(0, 0); // 重置力
    }
};

// 物理世界类
class PhysicsWorld {
public:
    std::vector<Body*> bodies; // 存储指针
    Vector2 gravity;

    PhysicsWorld(Vector2 g) : gravity(g) {}

    void addBody(Body* body) { // 接受指针
        bodies.push_back(body);
    }

    void update(float dt) {
        for (auto body : bodies) {
            body->applyForce(gravity * body->mass); // 使用箭头运算符
            body->update(dt);
        }

        // 简单的碰撞检测和响应
        for (size_t i = 0; i < bodies.size(); ++i) {
            for (size_t j = i + 1; j < bodies.size(); ++j) {
                handleCollision(*bodies[i], *bodies[j]);
            }
        }
    }

    void handleCollision(Body& a, Body& b) {
    Vector2 delta = b.position - a.position; // 从 a 指向 b 的向量
    float distance = delta.length();
    float minDistance = a.radius + b.radius;

    if (distance < minDistance) {
        // 计算法向量和相对速度
        Vector2 normal = delta.normalized();
        Vector2 relativeVelocity = b.velocity - a.velocity;
        float velocityAlongNormal = relativeVelocity.x * normal.x + relativeVelocity.y * normal.y;

        // 如果物体正在分离，不需要处理碰撞
        if (velocityAlongNormal > 0) return;

        // 弹性系数（完全弹性碰撞）
        float e = 1.0f;

        // 计算冲量
        float j = -(1 + e) * velocityAlongNormal;
        j /= (1 / a.mass + 1 / b.mass);

        // 应用冲量
        Vector2 impulse = normal * j;
        a.velocity = a.velocity - impulse * (1.0f / a.mass);
        b.velocity = b.velocity + impulse * (1.0f / b.mass);

        // 位置修正，防止物体重叠
        float penetration = minDistance - distance;
        Vector2 correction = normal * (penetration / (a.mass + b.mass)) * 0.8f; // 修正系数
        a.position = a.position - correction * (1.0f / a.mass);
        b.position = b.position + correction * (1.0f / b.mass);
    }
}
};

int main() {
    PhysicsWorld world(Vector2(0, -9.8f)); // 重力向下

    Body ball1(Vector2(0, 10), 1.0f, 1.0f);
    Body ball2(Vector2(1.5, 10), 1.0f, 1.0f);

    world.addBody(&ball1); // 传递指针
    world.addBody(&ball2); // 传递指针

    float dt = 0.01f;
    for (int i = 0; i < 1000; ++i) {
        world.update(dt);

        // 直接访问 ball1 和 ball2
        std::cout << ball1.position.x << "," << ball1.position.y << " "
                  << ball2.position.x << "," << ball2.position.y << std::endl;
    }

    return 0;
}