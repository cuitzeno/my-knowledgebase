---
title: "Java/Spring Boot Security 实战"
parent: "服务与开发安全"
grand_parent: "Web 安全与开发基础实战知识库"
nav_order: 3
---

# Java/Spring Boot Security 实战

## 一句话定义
把前面原则落到 Java/Spring Boot：**Spring Security 用过滤器链统一安全**；正确做法是——强哈希密码、方法级授权、保留 CSRF/CORS/安全头配置、密钥外置。

## 核心架构 / 工作原理

```mermaid
graph TD
  A[Spring Security 核心] --> B[过滤器链 Filter Chain]
  B --> B1[SecurityContextPersistenceFilter: 会话上下文]
  B --> B2[UsernamePasswordAuthenticationFilter: 表单登录]
  B --> B3[BasicAuthenticationFilter: Basic Auth]
  B --> B4[BearerTokenAuthenticationFilter: JWT/OAuth2]
  B --> B5[CsrfFilter: CSRF 保护]
  B --> B6[CorsFilter: CORS 处理]
  B --> B7[HeaderWriterFilter: 安全响应头]
  B --> B8[ExceptionTranslationFilter: 认证/授权异常转 HTTP 码]
  B --> B9[FilterSecurityInterceptor: URL/方法级授权拦截]
  
  A --> C[认证 Authentication]
  C --> C1[AuthenticationManager -> AuthenticationProvider -> UserDetailsService]
  C --> C2[PasswordEncoder: bcrypt/Argon2/PBKDF2]
  
  A --> D[授权 Authorization]
  D --> D1[URL 级: authorizeHttpRequests -> antMatchers/ regexMatchers]
  D --> D2[方法级: @PreAuthorize/@PostAuthorize/@Secured + SpEL]
  D --> D3[表达式: hasRole/hasAuthority/hasPermission/@bean.method()]
  
  A --> E[关键配置片段]
```

## 快速上手步骤

1. **密码存储**：
   ```java
   @Bean
   PasswordEncoder passwordEncoder() {
     // 强哈希：bcrypt(默认 10 轮) / Argon2 / PBKDF2
     return new BCryptPasswordEncoder(12); // 或 new Argon2PasswordEncoder()
   }
   // 禁用：NoOpPasswordEncoder / MD5 / SHA-1 / 明文
   ```
2. **SecurityFilterChain 配置 (Spring Boot 3.x)**：
   ```java
   @Bean
   SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
     http
       // 1. 授权规则：最小权限、方法级优先
       .authorizeHttpRequests(auth -> auth
         .requestMatchers("/actuator/health").permitAll()
         .requestMatchers("/admin/**").hasRole("ADMIN")
         .requestMatchers("/api/**").authenticated()
         .anyRequest().authenticated()
       )
       
       // 2. CSRF：状态化应用保留；无状态 JWT API 可关闭
       .csrf(csrf -> csrf
         .ignoringRequestMatchers("/api/**") // 仅无状态 API 关闭
         .csrfTokenRepository(CookieCsrfTokenRepository.withHttpOnlyFalse())
       )
       
       // 3. 安全头：HSTS/CSP/X-Frame 等
       .headers(headers -> headers
         .httpStrictTransportSecurity(hsts -> hsts
           .includeSubDomains(true).maxAgeInSeconds(63072000))
         .contentSecurityPolicy(csp -> csp
           .policyDirectives("default-src 'self'; script-src 'self' 'nonce-{nonce}'; ...")
         )
         .frameOptions(frame -> frame.sameOrigin())
         .referrerPolicy(rp -> rp.policy(ReferrerPolicy.STRICT_ORIGIN_WHEN_CROSS_ORIGIN))
       )
       
       // 4. OAuth2 Resource Server (JWT 鉴权)
       .oauth2ResourceServer(oauth2 -> oauth2
         .jwt(jwt -> jwt
           .decoder(jwtDecoder()) // NimbusJwtDecoder from JWKS
           .jwtAuthenticationConverter(jwtAuthenticationConverter()) // scope->authorities
         )
       )
       
       // 5. 会话管理：无状态 API 用 STATELESS
       .sessionManagement(sess -> sess
         .sessionCreationPolicy(SessionCreationPolicy.STATELESS)
       )
       
       // 6. 表单登录/登出 (传统 Web 保留)
       .formLogin(form -> form.loginPage("/login").permitAll())
       .logout(logout -> logout.logoutSuccessUrl("/").permitAll());
       
     return http.build();
   }
   
   // JWT Decoder from JWKS
   @Bean
   NimbusJwtDecoder jwtDecoder() {
     return NimbusJwtDecoder.withJwkSetUri("https://auth.example.com/.well-known/jwks.json").build();
   }
   
   // Scope -> Authority 映射
   @Bean
   JwtAuthenticationConverter jwtAuthenticationConverter() {
     var converter = new JwtAuthenticationConverter();
     converter.setJwtGrantedAuthoritiesConverter(jwt -> {
       var scopes = jwt.getClaimAsStringList("scope").orElse(List.of());
       return scopes.stream()
         .map(s -> new SimpleGrantedAuthority("SCOPE_" + s))
         .collect(Collectors.toList());
     });
     return converter;
   }
   
   // 方法级授权示例
   @PreAuthorize("hasRole('ADMIN')")
   @PreAuthorize("hasAuthority('SCOPE_write:orders')")
   @PreAuthorize("@orderService.isOwner(#orderId, authentication.name)")
   public void deleteOrder(Long orderId) { ... }
   ```
3. **密钥与配置外置**：
   ```yaml
   # application.yml (不入库敏感值)
   spring:
     security:
       oauth2:
         resourceserver:
           jwt:
             jwk-set-uri: ${JWK_SET_URI:https://auth.example.com/.well-known/jwks.json}
   # 密钥/Secret 放配置中心/环境变量/K8s Secrets
   ```
4. **常用依赖**：
   ```gradle
   implementation 'org.springframework.boot:spring-boot-starter-security'
   implementation 'org.springframework.boot:spring-boot-starter-oauth2-resource-server'
   implementation 'org.springframework.security:spring-security-oauth2-jose' // Nimbus
   implementation 'org.springframework.security:spring-security-oauth2-client' // 客户端
   testImplementation 'org.springframework.security:spring-security-test'
   ```

## 踩坑避坑指南

| 场景 | 问题现象 | 原因 | 解决/最佳实践 |
|------|----------|------|---------------|
| 加了 Spring Security 就安全 | 默认配置仍需按业务收紧(如暴露的 actuator) | 过度信任默认 | **显式收紧**：关闭多余端点、显式授权规则、保留安全头/CSRF |
| 只在 URL 层授权 | 内部服务调用/反射绕过 URL 拦截 | 粒度太粗 | **方法级注解 `@PreAuthorize`** 做细粒度授权，防内部调用越权 |
| 前后端分离就不需要 CSRF | Cookie 会话/状态化鉴权仍需 CSRF | 认知偏差 | **凭证机制决定**：Cookie/Session=需 CSRF；纯 JWT Bearer=可关闭 |
| 密码用弱哈希/明文 | `NoOpPasswordEncoder` / MD5 / SHA1 | 遗留/图省事 | **强制 `BCryptPasswordEncoder(12+)` 或 `Argon2PasswordEncoder`** |
| 密钥/Secret 写配置文件入库 | Git 泄露 → 全系统失控 | 配置管理缺失 | **外置密钥**：环境变量/配置中心/K8s Secrets/Vault；本地用 `.env` 不入库 |
| actuator 暴露敏感端点 | `/actuator/env` `/actuator/heapdump` 泄露配置/内存 | 默认暴露过多 | **显式配置**：`management.endpoints.web.exposure.include=health,info` |

## 替代方案对比

| 维度 | Spring Security | Apache Shiro | Quarkus Security | 手写 Filter/Interceptor |
|------|-----------------|--------------|------------------|------------------------|
| 生态成熟度 | 极高(Spring 标配) | 中(维护慢) | 高(Quarkus 原生) | 低(易漏/难维护) |
| 过滤器链 | 标准 Servlet Filter | 自有 Filter | Vert.x/Undertow Filter | 自定义 |
| 方法级授权 | `@PreAuthorize` + SpEL | `@RequiresPermissions` | `@RolesAllowed`/`@Permit` | 无(需自行实现) |
| OAuth2/JWT | 原生 Resource Server/Client | 需插件/手写 | 原生 SmallRye JWT | 手写 |
| 响应式支持 | Spring WebFlux 全支持 | 弱 | 原生响应式 | 需自行适配 |
| 学习曲线 | 中高(概念多) | 中 | 中低 | 低(但易坑) |

---

> 参考来源：https://www.marcobehler.com/guides/spring-security

*系列完：服务与开发安全*