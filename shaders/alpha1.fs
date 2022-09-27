#version 330 core
out vec4 FragColor;
in vec2 TexCoords;

struct Material{
    sampler2D texture_diffuse0;
    vec3 ambient_color;
    vec3 diffuse_color;
};

uniform Material material;

void main()
{
    //vec3 diffuse = material.diffuse_color * vec3(1, 1, 1);
    //vec3 ambient = material.ambient_color * vec3(0.2, 0.2, 0.2);
    //vec3 result = (ambient + diffuse) * vec3(texture(material.texture_diffuse0, TexCoords));
    //vec4 texColor = texture(material.texture_diffuse0, TexCoords);
    //if(texColor.a < 0.1 ){
    //    discard;
    //}
    FragColor = vec4(vec3(texture(material.texture_diffuse0, TexCoords)), 1.0);
}