// physics_engine.cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>

// 二维向量结构体
struct Vector2 {
    float x, y;
    
    Vector2(float x = 0, float y = 0) : x(x), y(y) {}
    
    Vector2 operator+(const Vector2& other) const {
        return Vector2(x + other.x, y + other.y);
    }
    
    Vector2 operator-(const Vector2& other) const {
        return Vector2(x - other.x, y - other.y);
    }
    
    Vector2 operator*(float scalar) const {
        return Vector2(x * scalar, y * scalar);
    }
    
    float magnitude() const {
        return std::sqrt(x*x + y*y);
    }
    
    Vector2 normalized() const {
        float mag = magnitude();
        return mag > 0 ? (*this) * (1.0f / mag) : Vector2();
    }
};

// 碰撞形状基类
struct Collider {
    enum Type { CIRCLE, AABB } type;
    Vector2 position;
};

// 圆形碰撞体
struct Circle : public Collider {
    float radius;
    
    Circle(float r = 1.0f) : radius(r) {
        type = Collider::CIRCLE;
    }
};

// 轴对齐包围盒（AABB）
struct AABB : public Collider {
    Vector2 size;
    
    AABB(Vector2 s = Vector2(1,1)) : size(s) {
        type = Collider::AABB;
    }
};

// 刚体类
class RigidBody {
public:
    Vector2 position;
    Vector2 velocity;
    float mass;
    float restitution;
    Collider* collider;
    bool collisionThisStep = false;

    RigidBody(Vector2 pos = Vector2(), Vector2 vel = Vector2(), 
             float m = 1.0f, float rest = 0.8f)
        : position(pos), velocity(vel), mass(m), restitution(rest), collider(nullptr) {}

    void applyForce(Vector2 force) {
        velocity = velocity + force * (1.0f / mass);
    }

    void update(float deltaTime) {
        position = position + velocity * deltaTime;
        if(collider) collider->position = position;
    }
};

// 物理引擎类
class PhysicsEngine {
private:
    std::vector<RigidBody*> bodies;
    Vector2 gravity;
    std::ofstream dataFile;
    float totalTime = 0.0f;

    bool checkCollision(Circle* a, Circle* b, Vector2& normal) {
        Vector2 delta = b->position - a->position;
        float distance = delta.magnitude();
        float minDistance = a->radius + b->radius;
        
        if (distance < minDistance) {
            normal = delta.normalized();
            return true;
        }
        return false;
    }

    bool checkCollision(Circle* circle, AABB* box, Vector2& normal) {
        Vector2 closestPoint;
        closestPoint.x = std::max(box->position.x - box->size.x/2, 
                                std::min(circle->position.x, box->position.x + box->size.x/2));
        closestPoint.y = std::max(box->position.y - box->size.y/2, 
                                std::min(circle->position.y, box->position.y + box->size.y/2));

        Vector2 delta = circle->position - closestPoint;
        float distance = delta.magnitude();
        
        if (distance < circle->radius) {
            normal = delta.normalized();
            return true;
        }
        return false;
    }

    bool checkCollision(AABB* a, AABB* b, Vector2& normal) {
        bool collisionX = a->position.x + a->size.x/2 > b->position.x - b->size.x/2 &&
                         a->position.x - a->size.x/2 < b->position.x + b->size.x/2;
        
        bool collisionY = a->position.y + a->size.y/2 > b->position.y - b->size.y/2 &&
                         a->position.y - a->size.y/2 < b->position.y + b->size.y/2;

        if (collisionX && collisionY) {
            Vector2 delta = b->position - a->position;
            if (std::abs(delta.x) > std::abs(delta.y)) {
                normal = Vector2(delta.x > 0 ? 1 : -1, 0);
            } else {
                normal = Vector2(0, delta.y > 0 ? 1 : -1);
            }
            return true;
        }
        return false;
    }

public:
    PhysicsEngine(Vector2 g = Vector2(0, -9.8f)) : gravity(g) {
        dataFile.open("physics_data.csv");
        dataFile << "time,obj_id,x,y,collision\n";
    }

    ~PhysicsEngine() {
        dataFile.close();
    }

    void addBody(RigidBody* body) {
        bodies.push_back(body);
    }

    void step(float deltaTime) {
        totalTime += deltaTime;

        for (auto body : bodies) {
            body->applyForce(gravity * body->mass);
            body->collisionThisStep = false;
        }

        for (auto body : bodies) {
            body->update(deltaTime);
        }

        for (size_t i = 0; i < bodies.size(); ++i) {
            for (size_t j = i+1; j < bodies.size(); ++j) {
                RigidBody* a = bodies[i];
                RigidBody* b = bodies[j];
                Vector2 normal;
                bool collision = false;

                if (a->collider && b->collider) {
                    if (a->collider->type == Collider::CIRCLE && 
                        b->collider->type == Collider::CIRCLE) {
                        collision = checkCollision(
                            static_cast<Circle*>(a->collider),
                            static_cast<Circle*>(b->collider),
                            normal);
                    }
                    else if (a->collider->type == Collider::CIRCLE && 
                            b->collider->type == Collider::AABB) {
                        collision = checkCollision(
                            static_cast<Circle*>(a->collider),
                            static_cast<AABB*>(b->collider),
                            normal);
                    }
                    else if (a->collider->type == Collider::AABB && 
                            b->collider->type == Collider::CIRCLE) {
                        collision = checkCollision(
                            static_cast<Circle*>(b->collider),
                            static_cast<AABB*>(a->collider),
                            normal);
                    }
                    else if (a->collider->type == Collider::AABB && 
                            b->collider->type == Collider::AABB) {
                        collision = checkCollision(
                            static_cast<AABB*>(a->collider),
                            static_cast<AABB*>(b->collider),
                            normal);
                    }
                }

                if (collision) {
                    a->collisionThisStep = true;
                    b->collisionThisStep = true;

                    Vector2 rv = b->velocity - a->velocity;
                    float velAlongNormal = rv.x * normal.x + rv.y * normal.y;

                    if (velAlongNormal > 0) continue;

                    float e = std::min(a->restitution, b->restitution);
                    float j = -(1 + e) * velAlongNormal;
                    j /= 1/a->mass + 1/b->mass;

                    Vector2 impulse = normal * j;
                    a->velocity = a->velocity - impulse * (1.0f / a->mass);
                    b->velocity = b->velocity + impulse * (1.0f / b->mass);
                }
            }
        }

        for (size_t idx = 0; idx < bodies.size(); ++idx) {
            RigidBody* body = bodies[idx];
            dataFile << totalTime << "," 
                     << idx << ","
                     << body->position.x << ","
                     << body->position.y << ","
                     << (body->collisionThisStep ? 1 : 0) << "\n";
        }
    }
};

int main() {
    PhysicsEngine engine;
    
    RigidBody* ball = new RigidBody(Vector2(0, 5), Vector2(2, 0), 1.0f);
    ball->collider = new Circle(0.5f);
    
    RigidBody* ground = new RigidBody(Vector2(0, -0.5f), Vector2(), 1000.0f);
    ground->collider = new AABB(Vector2(10, 1));

    engine.addBody(ball);
    engine.addBody(ground);

    for (int i = 0; i < 300; ++i) {
        engine.step(0.016f);
    }

    delete ball->collider;
    delete ground->collider;
    delete ball;
    delete ground;

    return 0;
}